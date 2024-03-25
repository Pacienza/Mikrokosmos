import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random

root = tk.Tk()
root.title("Mikrokosmos - Tarot Digital")
root.geometry("800x600")
style = ttk.Style(theme="vapor")

arcanosMaiores = [
    'O Louco', 'O Mago', 'A Sacerdotisa', 'A Imperatriz',
    'O Imperador', 'O Hierofante', 'Os Enamorados', 'A Carruagem',
    'A Justiça', 'O Eremita', 'Roda da Fortuna', 'A Força',
    'O Enforcado', 'Morte', 'A Temperança', 'O Diabo',
    'A Torre', 'A Estrela', 'A Lua', 'O Sol', 'O Julgamento', 'O Mundo'
]

resultado_label = ttk.Label(root, text="", bootstyle=LIGHT)
resultado_label.pack(pady=10)

def templo():
    numero_cartas = 7
    cartas_aleatorias = random.sample(arcanosMaiores, numero_cartas)
    resultado_label.config(text=cartas_aleatorias)

def peladan():
    numero_cartas = 5
    cartas_aleatorias = random.sample(arcanosMaiores, numero_cartas)
    resultado_label.config(text=cartas_aleatorias)

def avulso():
    carta_aleatoria = random.choice(arcanosMaiores)
    resultado_label.config(text=carta_aleatoria)
    return carta_aleatoria

# Correção: passa a função sem os parênteses
b1 = ttk.Button(root, text="Templo de Afrodite", bootstyle=LIGHT, command=templo)
b1.pack(side=tk.LEFT, padx=10, pady=10)

b2 = ttk.Button(root, text="Peladan", bootstyle=LIGHT, command=peladan)
b2.pack(side=tk.LEFT, padx=10, pady=10)

b3 = ttk.Button(root, text="Avulsa", bootstyle=LIGHT, command=avulso)
b3.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
