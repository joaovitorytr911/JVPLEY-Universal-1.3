# JVPLEY Universal 1.3 — interface estilo central CarPlay
# Interface visual funcional; GPS, música e telemetria ainda aguardam integração.
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import math

BG = "#050d18"
PANEL = "#0b1b2c"
PANEL_2 = "#10263b"
CYAN = "#35d9ff"
WHITE = "#edf8ff"
MUTED = "#91aabd"
BORDER = "#17415c"
GREEN = "#58e0a0"

root = tk.Tk()
root.title("JVPLEY Universal 1.3")
root.geometry("1280x800")
root.minsize(980, 650)
root.configure(bg=BG)

# ---------- Barra superior ----------
top = tk.Frame(root, bg="#081523", height=66)
top.pack(fill="x")
top.pack_propagate(False)

brand = tk.Frame(top, bg="#081523")
brand.pack(side="left", padx=26)
tk.Label(brand, text="JVPLEY", font=("Segoe UI", 22, "bold"), fg=CYAN, bg="#081523").pack(side="left")
tk.Label(brand, text="  UNIVERSAL", font=("Segoe UI", 10, "bold"), fg=WHITE, bg="#081523").pack(side="left", pady=(8, 0))

status = tk.Frame(top, bg="#081523")
status.pack(side="right", padx=26)
tk.Label(status, text="●", font=("Segoe UI", 10), fg=GREEN, bg="#081523").pack(side="left")
tk.Label(status, text="SISTEMA LOCAL", font=("Segoe UI", 9, "bold"), fg=MUTED, bg="#081523").pack(side="left", padx=(5, 18))
digital_clock = tk.Label(status, text="--:--", font=("Segoe UI", 18, "bold"), fg=WHITE, bg="#081523")
digital_clock.pack(side="left")

# ---------- Cabeçalho ----------
intro = tk.Frame(root, bg=BG)
intro.pack(fill="x", padx=28, pady=(20, 12))
tk.Label(intro, text="Sua viagem. Seu controle.", font=("Segoe UI", 23, "bold"), fg=WHITE, bg=BG).pack(anchor="w")
tk.Label(intro, text="CENTRAL MULTIMÍDIA JVPLEY  •  INTERFACE 1.3", font=("Segoe UI", 9, "bold"), fg=CYAN, bg=BG).pack(anchor="w", pady=(3, 0))

# ---------- Área principal ----------
body = tk.Frame(root, bg=BG)
body.pack(fill="both", expand=True, padx=26, pady=(4, 12))
body.grid_columnconfigure(0, weight=3)
body.grid_columnconfigure(1, weight=2)
body.grid_rowconfigure(0, weight=1)

left = tk.Frame(body, bg=BG)
left.grid(row=0, column=0, sticky="nsew", padx=(0, 14))
right = tk.Frame(body, bg=BG)
right.grid(row=0, column=1, sticky="nsew")

tk.Label(left, text="APLICATIVOS", font=("Segoe UI", 10, "bold"), fg=MUTED, bg=BG).pack(anchor="w", pady=(0, 10))

apps = tk.Frame(left, bg=BG)
apps.pack(fill="both", expand=True)
for c in range(2):
    apps.grid_columnconfigure(c, weight=1, uniform="app")
for r in range(2):
    apps.grid_rowconfigure(r, weight=1, uniform="app")

message = tk.StringVar(value="Central pronta • módulos externos ainda não conectados")

def select_app(name, detail):
    message.set(name + " • " + detail)

def app_card(parent, row, col, symbol, title, subtitle, accent=CYAN):
    card = tk.Frame(parent, bg=PANEL, highlightbackground=BORDER, highlightthickness=1, cursor="hand2")
    card.grid(row=row, column=col, sticky="nsew", padx=7, pady=7)
    inner = tk.Frame(card, bg=PANEL)
    inner.pack(fill="both", expand=True, padx=18, pady=16)
    icon = tk.Label(inner, text=symbol, font=("Segoe UI Emoji", 30), fg=accent, bg=PANEL)
    icon.pack(anchor="w")
    tk.Label(inner, text=title, font=("Segoe UI", 17, "bold"), fg=WHITE, bg=PANEL).pack(anchor="w", pady=(9, 2))
    tk.Label(inner, text=subtitle, font=("Segoe UI", 9), fg=MUTED, bg=PANEL, wraplength=260, justify="left").pack(anchor="w")
    for widget in (card, inner, icon):
        widget.bind("<Button-1>", lambda event, n=title, d=subtitle: select_app(n, d))

app_card(apps, 0, 0, "⌖", "NAVEGAÇÃO", "GPS e mapas • integração pendente")
app_card(apps, 0, 1, "♫", "MÚSICA", "Central de áudio • integração pendente", "#67e6bd")
app_card(apps, 1, 0, "◈", "TELEMETRIA", "Euro Truck Simulator 2 • plugin em desenvolvimento", "#69a8ff")
app_card(apps, 1, 1, "⚙", "CONFIGURAÇÕES", "Preferências da central", "#b9a0ff")

# ---------- Painel lateral: relógio e viagem ----------
clock_box = tk.Frame(right, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
clock_box.pack(fill="both", expand=True)
tk.Label(clock_box, text="RELÓGIO", font=("Segoe UI", 10, "bold"), fg=CYAN, bg=PANEL).pack(anchor="w", padx=18, pady=(16, 2))
clock_canvas = tk.Canvas(clock_box, width=220, height=220, bg=PANEL, highlightthickness=0)
clock_canvas.pack(pady=(2, 4))
date_label = tk.Label(clock_box, text="", font=("Segoe UI", 11, "bold"), fg=WHITE, bg=PANEL)
date_label.pack(pady=(0, 12))
tk.Frame(clock_box, bg=BORDER, height=1).pack(fill="x", padx=18, pady=4)
tk.Label(clock_box, text="STATUS DA VIAGEM", font=("Segoe UI", 9, "bold"), fg=MUTED, bg=PANEL).pack(anchor="w", padx=18, pady=(9, 5))
tk.Label(clock_box, text="Aguardando conexão com o ETS2", font=("Segoe UI", 10), fg=WHITE, bg=PANEL, wraplength=280, justify="left").pack(anchor="w", padx=18, pady=(0, 14))

# ---------- Barra inferior estilo dock ----------
bottom = tk.Frame(root, bg="#081523", height=62)
bottom.pack(fill="x", side="bottom")
bottom.pack_propagate(False)
dock = tk.Frame(bottom, bg="#081523")
dock.pack(expand=True)
for symbol, label in [("⌂", "INÍCIO"), ("⌖", "MAPA"), ("♫", "ÁUDIO"), ("◈", "JOGO")]:
    item = tk.Frame(dock, bg="#081523", padx=22)
    item.pack(side="left", pady=6)
    tk.Label(item, text=symbol, font=("Segoe UI Emoji", 17), fg=CYAN, bg="#081523").pack()
    tk.Label(item, text=label, font=("Segoe UI", 7, "bold"), fg=MUTED, bg="#081523").pack()

statusbar = tk.Label(root, textvariable=message, font=("Segoe UI", 8), fg=MUTED, bg=BG, anchor="w")
statusbar.pack(fill="x", padx=30, pady=(0, 5))

def draw_clock(now):
    clock_canvas.delete("all")
    cx = cy = 110
    clock_canvas.create_oval(12, 12, 208, 208, outline=BORDER, width=4)
    clock_canvas.create_oval(18, 18, 202, 202, outline=CYAN, width=1)
    for number in range(1, 13):
        angle = math.radians(number * 30 - 90)
        x = cx + math.cos(angle) * 77
        y = cy + math.sin(angle) * 77
        clock_canvas.create_text(x, y, text=str(number), fill=WHITE, font=("Segoe UI", 11, "bold"))
    for tick in range(60):
        angle = math.radians(tick * 6 - 90)
        inner = 86 if tick % 5 == 0 else 91
        x1, y1 = cx + math.cos(angle) * inner, cy + math.sin(angle) * inner
        x2, y2 = cx + math.cos(angle) * 96, cy + math.sin(angle) * 96
        clock_canvas.create_line(x1, y1, x2, y2, fill=CYAN if tick % 5 == 0 else BORDER, width=2 if tick % 5 == 0 else 1)
    sec = now.second + now.microsecond / 1_000_000
    minute = now.minute + sec / 60
    hour = now.hour % 12 + minute / 60
    def hand(value, units, length, color, width):
        angle = math.radians(value * 360 / units - 90)
        clock_canvas.create_line(cx, cy, cx + math.cos(angle) * length, cy + math.sin(angle) * length, fill=color, width=width, capstyle=tk.ROUND)
    hand(hour, 12, 43, WHITE, 5)
    hand(minute, 60, 65, CYAN, 3)
    hand(sec, 60, 78, "#ff647c", 1)
    clock_canvas.create_oval(cx-4, cy-4, cx+4, cy+4, fill=CYAN, outline=WHITE)

def tick():
    now = datetime.now()
    digital_clock.config(text=now.strftime("%H:%M"))
    date_label.config(text=now.strftime("%d/%m/%Y"))
    draw_clock(now)
    root.after(200, tick)

# ---------- Tela de ignição estilo CarPlay ----------
# Nesta primeira versão, a ignição é simulada ao abrir o aplicativo.
# A leitura real do sinal elétrico do caminhão/ETS2 será integrada depois.
main_widgets = [top, intro, body, bottom, statusbar]
for widget in main_widgets:
    widget.pack_forget()

splash = tk.Frame(root, bg="#000000")
splash.place(relx=0, rely=0, relwidth=1, relheight=1)
splash_title = tk.Label(splash, text="", font=("Bahnschrift SemiBold", 42, "bold"), fg="#FFFFFF", bg="#000000")
splash_title.place(relx=0.5, rely=0.46, anchor="center")
splash_subtitle = tk.Label(splash, text="", font=("Bahnschrift SemiBold", 42, "bold"), fg="#FFFFFF", bg="#000000")
splash_subtitle.place(relx=0.5, rely=0.55, anchor="center")
splash_caption = tk.Label(splash, text="", font=("Segoe UI", 9), fg="#888888", bg="#000000")
splash_caption.place(relx=0.5, rely=0.66, anchor="center")

def reveal_ignition(text, label, index=0, done=None):
    label.config(text=text[:index])
    if index < len(text):
        root.after(95, lambda: reveal_ignition(text, label, index + 1, done))
    elif done:
        done()

def show_carplay_word():
    reveal_ignition("CARPLAY", splash_subtitle)

def enter_carplay():
    splash.destroy()
    top.pack(fill="x")
    intro.pack(fill="x", padx=28, pady=(20, 12))
    body.pack(fill="both", expand=True, padx=26, pady=(4, 12))
    bottom.pack(fill="x", side="bottom")
    statusbar.pack(fill="x", padx=30, pady=(0, 5))

reveal_ignition("ANDROID", splash_title, done=show_carplay_word)
splash_caption.config(text="INICIANDO CENTRAL MULTIMÍDIA")
root.after(5200, enter_carplay)

tick()
root.mainloop()
