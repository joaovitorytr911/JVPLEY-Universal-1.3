# JVPLEY Universal 1.3 - prototipo visual para Windows 11
# O relógio é funcional; GPS, áudio e telemetria continuam demonstrativos.
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import math

BG = "#07111f"
PANEL = "#0d2035"
CYAN = "#35d9ff"
WHITE = "#eaf7ff"
MUTED = "#8ca8bd"
RING = "#17415c"

root = tk.Tk()
root.title("JVPLEY Universal 1.3")
root.geometry("1120x760")
root.minsize(860, 620)
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")

header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=28, pady=(20, 8))

brand = tk.Frame(header, bg=BG)
brand.pack(side="left", anchor="nw")
tk.Label(brand, text="JVPLEY", font=("Segoe UI", 32, "bold"), fg=CYAN, bg=BG).pack(anchor="w")
tk.Label(brand, text="UNIVERSAL 1.3  |  CENTRAL MULTIMÍDIA", font=("Segoe UI", 10), fg=MUTED, bg=BG).pack(anchor="w")
digital_clock = tk.Label(brand, text="--:--:--", font=("Segoe UI", 20, "bold"), fg=WHITE, bg=BG)
digital_clock.pack(anchor="w", pady=(10, 0))

clock_panel = tk.Frame(header, bg=BG)
clock_panel.pack(side="right", padx=8)
clock_canvas = tk.Canvas(clock_panel, width=190, height=190, bg=BG, highlightthickness=0)
clock_canvas.pack()

tk.Label(root, text="BEM-VINDO À CENTRAL", font=("Segoe UI", 21, "bold"), fg=WHITE, bg=BG).pack(anchor="w", padx=30, pady=(12, 4))
tk.Label(root, text="Painel de demonstração • relógio em tempo real", font=("Segoe UI", 10), fg=MUTED, bg=BG).pack(anchor="w", padx=32)

main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True, padx=24, pady=20)

items = [
    ("NAVEGAÇÃO", "GPS e mapas", "Integração ainda não conectada"),
    ("MÚSICA", "Central de áudio", "Serviço de música ainda não conectado"),
    ("TELEMETRIA", "Euro Truck Simulator 2", "Aguardando integração real com o jogo"),
    ("CONEXÃO", "Multimídia", "Protótipo local — sem conexão com veículo"),
]
for i, (tag, title, detail) in enumerate(items):
    card = tk.Frame(main, bg=PANEL, highlightbackground=RING, highlightthickness=1)
    card.grid(row=i//2, column=i%2, sticky="nsew", padx=10, pady=10, ipadx=18, ipady=18)
    tk.Label(card, text=tag, font=("Segoe UI", 10, "bold"), fg=CYAN, bg=PANEL).pack(anchor="w", padx=18, pady=(14, 8))
    tk.Label(card, text=title, font=("Segoe UI", 19, "bold"), fg=WHITE, bg=PANEL).pack(anchor="w", padx=18)
    tk.Label(card, text=detail, font=("Segoe UI", 10), fg=MUTED, bg=PANEL, wraplength=390, justify="left").pack(anchor="w", padx=18, pady=(8, 14))
main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)
main.grid_rowconfigure(0, weight=1)
main.grid_rowconfigure(1, weight=1)

footer = tk.Label(root, text="JVPLEY • Construção inicial • Não usar nem operar durante a condução", font=("Segoe UI", 9), fg=MUTED, bg=BG)
footer.pack(pady=(0, 16))

def draw_analog_clock(now):
    clock_canvas.delete("all")
    cx = cy = 95
    radius = 82
    clock_canvas.create_oval(8, 8, 182, 182, outline=RING, width=3)
    clock_canvas.create_oval(14, 14, 176, 176, outline=CYAN, width=1)
    for number in range(1, 13):
        angle = math.radians(number * 30 - 90)
        tx = cx + math.cos(angle) * 65
        ty = cy + math.sin(angle) * 65
        clock_canvas.create_text(tx, ty, text=str(number), fill=WHITE, font=("Segoe UI", 10, "bold"))
    for tick in range(60):
        angle = math.radians(tick * 6 - 90)
        inner = 72 if tick % 5 == 0 else 77
        x1 = cx + math.cos(angle) * inner
        y1 = cy + math.sin(angle) * inner
        x2 = cx + math.cos(angle) * 80
        y2 = cy + math.sin(angle) * 80
        clock_canvas.create_line(x1, y1, x2, y2, fill=CYAN if tick % 5 == 0 else RING, width=2 if tick % 5 == 0 else 1)

    seconds = now.second + now.microsecond / 1_000_000
    minutes = now.minute + seconds / 60
    hours = (now.hour % 12) + minutes / 60

    def hand(value, units, length, color, width):
        angle = math.radians(value * 360 / units - 90)
        x = cx + math.cos(angle) * length
        y = cy + math.sin(angle) * length
        clock_canvas.create_line(cx, cy, x, y, fill=color, width=width, capstyle=tk.ROUND)

    hand(hours, 12, 39, WHITE, 5)
    hand(minutes, 60, 57, CYAN, 3)
    hand(seconds, 60, 68, "#ff647c", 1)
    clock_canvas.create_oval(cx-4, cy-4, cx+4, cy+4, fill=CYAN, outline=WHITE)

def update_clock():
    now = datetime.now()
    digital_clock.config(text=now.strftime("%H:%M:%S"))
    draw_analog_clock(now)
    root.after(200, update_clock)

update_clock()
root.mainloop()
