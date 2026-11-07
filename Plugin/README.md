# JVPLEY ETS2 Plugin

This folder contains the initial Windows x64 DLL project scaffold.

## Important status
The current DLL build is a **bootstrap/test DLL only**. It exports JVPLEY metadata, but it does not yet implement the SCS Telemetry SDK callbacks and ETS2 will not treat it as a working telemetry plugin.

## Required next implementation
1. Integrate the official SCS Telemetry SDK headers and sample.
2. Implement the SCS-required exported API functions and callback registration.
3. Publish telemetry to the JVPLEY desktop app through a documented local IPC interface.
4. Test with ETS2 1.61 (64-bit) before calling it compatible.

Do not install this bootstrap DLL in the game plugins folder expecting telemetry.
