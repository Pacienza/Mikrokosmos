import tkinter as tk
from tkinter import Toplevel, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random

root = tk.Tk()
root.title("Mikrokosmos - Tarot Digital")
root.geometry("512x512")
style = ttk.Style(theme="vapor")

title_label = ttk.Label(root, text="Mikrokosmos - Tarot Digital", font=("Arial", 30))
title_label.pack(pady=10)

footer_label = ttk.Label(root, text="Desenvolvido por Lucas Pacienza. 2024 \nTodos direitos reservados a VL Info®",
                         font=("Arial", 10))
footer_label.pack(side=tk.BOTTOM, pady=10)

arcanosMaiores = {
    'O Louco': 'img/major_arcana_fool (Personalizado).png',
    'O Mago': 'img/major_arcana_magician (Personalizado).png',
    'A Sacerdotisa': 'img/major_arcana_priestess (Personalizado).png',
    'A Imperatriz': 'img/major_arcana_empress (Personalizado).png',
    'O Imperador': 'img/major_arcana_emperor (Personalizado).png',
    'O Hierofante': 'img/major_arcana_hierophant (Personalizado).png',
    'Os Enamorados': 'img/major_arcana_lovers (Personalizado).png',
    'A Carruagem': 'img/major_arcana_chariot (Personalizado).png',
    'A Justiça': 'img/major_arcana_justice (Personalizado).png',
    'O Eremita': 'img/major_arcana_hermit (Personalizado).png',
    'Roda da Fortuna': 'img/major_arcana_fortune (Personalizado).png',
    'A Força': 'img/major_arcana_strength (Personalizado).png',
    'O Enforcado': 'img/major_arcana_hanged (Personalizado).png',
    'Morte': 'img/major_arcana_death (Personalizado).png',
    'A Temperança': 'img/major_arcana_temperance (Personalizado).png',
    'O Diabo': 'img/major_arcana_devil (Personalizado).png',
    'A Torre': 'img/major_arcana_temperance (Personalizado).png',
    'A Estrela': 'img/major_arcana_star (Personalizado).png',
    'A Lua': 'img/major_arcana_moon (Personalizado).png',
    'O Sol': 'img/major_arcana_sun (Personalizado).png',
    'O Julgamento': 'img/major_arcana_judgement (Personalizado).png',
    'O Mundo': 'img/major_arcana_world (Personalizado).png'
}

# noinspection PyArgumentList
resultado_label = ttk.Label(root, text="", bootstyle=LIGHT)
resultado_label.pack(pady=10)

intencoes = {}


def energisa_sistema():
    user_input = input_field.get()
    if len(user_input.strip()) == 0:
        messagebox.showinfo("Aviso!", "A intenção não pode ser vazia")
    else:
        intencoes[user_input] = user_input
        messagebox.showinfo("Confirmação", "Sistema energizado com a intenção, prossiga para a consulta")


input_field = ttk.Entry(root)
input_field.pack(pady=10)
store_button = ttk.Button(root, text="Enviar intenção para o sistema", bootstyle=LIGHT, command=energisa_sistema)
store_button.pack(side=tk.TOP, padx=10, pady=10)


def mostra_imagens(cartas, layout=None):
    new_window = Toplevel(root)
    new_window.title("Resultado Tiragem")
    if layout == 'templo':
        positions = [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2)]
    elif layout == 'peladan':
        positions = [(1, 0), (1, 1), (1, 2), (0, 1), (2, 1)]
    else:
        positions = [(i // 3, i % 3) for i in range(len(cartas))]

    for i, carta in enumerate(cartas):
        img = tk.PhotoImage(file=arcanosMaiores[carta])
        if layout in ['templo', 'peladan'] and i < len(positions):
            label = ttk.Label(new_window, image=img)
            label.grid(row=positions[i][0], column=positions[i][1])
        else:
            label = ttk.Label(new_window, image=img)
            label.grid(row=i // 3, column=i % 3)
        label.image = img


def tiragem_composta(numero_cartas):
    cartas_possiveis = list(arcanosMaiores.keys())
    cartas_aleatorias = random.sample(cartas_possiveis, numero_cartas)
    return cartas_aleatorias


def templo():
    numero_cartas = 7
    resultado_tiragem = tiragem_composta(numero_cartas)
    mostra_imagens(resultado_tiragem, 'templo')


def peladan():
    numero_cartas = 5
    resultado_tiragem = tiragem_composta(numero_cartas)
    mostra_imagens(resultado_tiragem, 'peladan')


def basico():
    numero_cartas = 3
    resultado_tiragem = tiragem_composta(numero_cartas)
    mostra_imagens(resultado_tiragem)


def avulso():
    carta_aleatoria = random.choice(list(arcanosMaiores.keys()))
    mostra_imagens([carta_aleatoria])


b1 = ttk.Button(root, text="Templo de Afrodite", bootstyle=LIGHT, command=templo)
b1.pack(side=tk.LEFT, padx=5, pady=5)

b2 = ttk.Button(root, text="Peladan", bootstyle=LIGHT, command=peladan)
b2.pack(side=tk.LEFT, padx=5, pady=5)

b3 = ttk.Button(root, text="Carta Avulsa", bootstyle=LIGHT, command=avulso)
b3.pack(side=tk.RIGHT, padx=10, pady=10)

b4 = ttk.Button(root, text="Consulta Basica", bootstyle=LIGHT, command=basico)
b4.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
