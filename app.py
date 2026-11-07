import tkinter as tk
from tkinter import ttk
from datetime import datetime

BG = "#07111f"
PANEL = "#0d2035"
CYAN = "#35d9ff"
WHITE = "#eaf7ff"
MUTED = "#8ca8bd"

root = tk.Tk()
root.title("JVPLEY Universal 1.3 - Protótipo")
root.geometry("1100x680")
root.minsize(820, 540)
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background=PANEL, foreground=WHITE, fieldbackground=PANEL)

header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=28, pady=(22, 10))
tk.Label(header, text="JVPLEY", font=("Segoe UI", 30, "bold"), fg=CYAN, bg=BG).pack(side="left")
tk.Label(header, text="UNIVERSAL 1.3  |  CENTRAL MULTIMÍDIA", font=("Segoe UI", 11), fg=MUTED, bg=BG).pack(side="left", padx=18, pady=(13, 0))
clock = tk.Label(header, font=("Segoe UI", 22, "bold"), fg=WHITE, bg=BG)
clock.pack(side="right")

tk.Label(root, text="BEM-VINDO À CENTRAL", font=("Segoe UI", 21, "bold"), fg=WHITE, bg=BG).pack(anchor="w", padx=30, pady=(22, 4))
tk.Label(root, text="Protótipo visual para Windows • dados de demonstração", font=("Segoe UI", 10), fg=MUTED, bg=BG).pack(anchor="w", padx=32)

main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True, padx=24, pady=24)

items = [
    ("NAVEGAÇÃO", "GPS e mapas", "Integração ainda não conectada"),
    ("MÚSICA", "Central de áudio", "Abra seu serviço de música separadamente"),
    ("TELEMETRIA", "Euro Truck Simulator 2", "Aguardando integração real com o jogo"),
    ("CONEXÃO", "Multimídia", "Protótipo local — sem conexão com veículo"),
]
for i, (tag, title, detail) in enumerate(items):
    card = tk.Frame(main, bg=PANEL, highlightbackground="#17415c", highlightthickness=1)
    card.grid(row=i//2, column=i%2, sticky="nsew", padx=10, pady=10, ipadx=18, ipady=22)
    tk.Label(card, text=tag, font=("Segoe UI", 10, "bold"), fg=CYAN, bg=PANEL).pack(anchor="w", padx=18, pady=(14, 8))
    tk.Label(card, text=title, font=("Segoe UI", 19, "bold"), fg=WHITE, bg=PANEL).pack(anchor="w", padx=18)
    tk.Label(card, text=detail, font=("Segoe UI", 10), fg=MUTED, bg=PANEL, wraplength=390, justify="left").pack(anchor="w", padx=18, pady=(8, 14))
main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)
main.grid_rowconfigure(0, weight=1)
main.grid_rowconfigure(1, weight=1)

footer = tk.Label(root, text="JVPLEY • Construção inicial • Não usar como sistema de navegação durante a condução", font=("Segoe UI", 9), fg=MUTED, bg=BG)
footer.pack(pady=(0, 18))

def update_clock():
    clock.config(text=datetime.now().strftime("%H:%M:%S"))
    root.after(1000, update_clock)

update_clock()
root.mainloop()
