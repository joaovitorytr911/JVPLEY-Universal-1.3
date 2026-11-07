//! JVPLEY Universal 1.3 — real SCS ETS2 telemetry plugin.
//! First milestone: subscribe to live game telemetry and write rate-limited snapshots to game.log.txt.
//! App transport (named pipe/shared memory) will be added after this DLL is built and tested.

use scs_sdk_plugin::sdk::{TelemetryApiVersion, channels, game};
use scs_sdk_plugin::{
    ChannelUpdate, Game, GameCompatibility, PluginCompatibility, PluginContext,
    PluginMetadata, PluginResult, TelemetryEvent, TelemetryEventKind, TelemetryPlugin,
    export_plugin,
};

const LOG_INTERVAL_US: u64 = 1_000_000;

static SUPPORTED_GAMES: [GameCompatibility; 1] = [GameCompatibility::new(
    Game::EuroTruckSimulator2,
    game::ets2::V1_14,
)];

#[derive(Default)]
struct JvpleyTelemetry {
    speed_mps: f32,
    rpm: f32,
    gear: i32,
    nav_distance_m: f32,
    nav_time_s: f32,
    nav_speed_limit_mps: f32,
    render_time_us: u64,
    last_log_us: Option<u64>,
    paused: bool,
}

impl TelemetryPlugin for JvpleyTelemetry {
    fn metadata(&self) -> PluginMetadata {
        PluginMetadata::new("JVPLEY Universal ETS2 Telemetry", env!("CARGO_PKG_VERSION"))
    }

    fn compatibility(&self) -> PluginCompatibility {
        PluginCompatibility::new(TelemetryApiVersion::V1_01, &SUPPORTED_GAMES)
    }

    fn initialize(&mut self, context: &mut PluginContext<'_>) -> PluginResult {
        *self = Self::default();
        context.subscribe_event(TelemetryEventKind::FrameStart)?;
        context.subscribe_event(TelemetryEventKind::FrameEnd)?;
        context.subscribe_event(TelemetryEventKind::Paused)?;
        context.subscribe_event(TelemetryEventKind::Started)?;
        context.subscribe(channels::truck::SPEED)?;
        context.subscribe(channels::truck::ENGINE_RPM)?;
        context.subscribe(channels::truck::ENGINE_GEAR)?;
        context.subscribe(channels::truck::NAVIGATION_DISTANCE)?;
        context.subscribe(channels::truck::NAVIGATION_TIME)?;
        context.subscribe(channels::truck::NAVIGATION_SPEED_LIMIT)?;
        context.message(format_args!("[JVPLEY] SCS telemetry plugin initialized"));
        Ok(())
    }

    fn channel(&mut self, _context: &mut PluginContext<'_>, update: ChannelUpdate<'_>) {
        if let Some(value) = update.value(channels::truck::SPEED) {
            self.speed_mps = value;
        } else if let Some(value) = update.value(channels::truck::ENGINE_RPM) {
            self.rpm = value;
        } else if let Some(value) = update.value(channels::truck::ENGINE_GEAR) {
            self.gear = value;
        } else if let Some(value) = update.value(channels::truck::NAVIGATION_DISTANCE) {
            self.nav_distance_m = value;
        } else if let Some(value) = update.value(channels::truck::NAVIGATION_TIME) {
            self.nav_time_s = value;
        } else if let Some(value) = update.value(channels::truck::NAVIGATION_SPEED_LIMIT) {
            self.nav_speed_limit_mps = value;
        }
    }

    fn event(&mut self, context: &mut PluginContext<'_>, event: TelemetryEvent<'_>) {
        match event {
            TelemetryEvent::FrameStart(frame) => {
                self.render_time_us = frame.render_time();
                if frame.timer_restarted() { self.last_log_us = None; }
            }
            TelemetryEvent::Paused => {
                self.paused = true;
                context.message(format_args!("[JVPLEY] telemetry paused"));
            }
            TelemetryEvent::Started => {
                self.paused = false;
                context.message(format_args!("[JVPLEY] telemetry started"));
            }
            TelemetryEvent::FrameEnd if !self.paused => {
                if let Some(last) = self.last_log_us {
                    if self.render_time_us.saturating_sub(last) < LOG_INTERVAL_US { return; }
                }
                self.last_log_us = Some(self.render_time_us);
                context.message(format_args!(
                    "[JVPLEY] speed={:.1} km/h rpm={:.0} gear={} nav_distance={:.0} m nav_time={:.0} s speed_limit={:.1} km/h",
                    self.speed_mps * 3.6, self.rpm, self.gear, self.nav_distance_m,
                    self.nav_time_s, self.nav_speed_limit_mps * 3.6
                ));
            }
            _ => {}
        }
    }

    fn shutdown(&mut self, context: &mut PluginContext<'_>) {
        context.message(format_args!("[JVPLEY] telemetry plugin shutdown"));
        *self = Self::default();
    }
}

export_plugin!(JvpleyTelemetry::default());
