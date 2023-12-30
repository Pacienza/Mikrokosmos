import random
from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title("MIKROKOSMOS TAROT")
        self.root.geometry('1080x700')
        self.root.resizable(True, True)
        self.root.maxsize(width= 1360, height= 768)
        self.root.minsize(width= 800, height= 600)

Application()

arcanosMaiores = [
    'O Louco',
    'O Mago',
    'A Sacerdotisa',
    'A Imperatriz',
    'O Imperador',
    'O Hierofante',
    'Os Enamorados',
    'A Carruagem',
    'A Justiça',
    'O Eremita',
    'Roda da Fortuna',
    'A Força',
    'O Enforcado',
    'Morte',
    'A Temperança',
    'O Diabo',
    'A Torre',
    'A Estrela',
    'A Lua',
    'O Sol',
    'O Julgamento',
    'O Mundo'
]
arcanosMenores = [
    'Ás de Copas',
    'Ás de Ouros',
    'Ás de Paus',
    'Ás de Espadas',
    'Rei de Copas',
    'Rei de Ouros',
    'Rei de Paus',
    'Rei de Espadas',
    'Dama de Copas',
    'Dama de Ouros',
    'Dama de Paus',
    'Dama de Espadas',
    'Valete de Copas',
    'Valete de Ouros',
    'Valete de Paus',
    'Valete de Espadas',
    '1 de Copas',
    '1 de Ouros',
    '1 de Paus',
    '1 de Espadas',
    '2 de Copas',
    '2 de Ouros',
    '2 de Paus',
    '2 de Espadas',
    '3 de Copas',
    '3 de Ouros',
    '3 de Paus',
    '3 de Espadas',
    '4 de Copas',
    '4 de Ouros',
    '4 de Paus',
    '4 de Espadas',
    '5 de Copas',
    '5 de Ouros',
    '5 de Paus',
    '5 de Espadas',
    '6 de Copas',
    '6 de Ouros',
    '6 de Paus',
    '6 de Espadas',
    '7 de Copas',
    '7 de Ouros',
    '7 de Paus',
    '7 de Espadas',
    '8 de Copas',
    '8 de Ouros',
    '8 de Paus',
    '8 de Espadas',
    '9 de Copas',
    '9 de Ouros',
    '9 de Paus',
    '9 de Espadas',
    '10 de Copas',
    '10 de Ouros',
    '10 de Paus',
    '10 de Espadas',
]

def tiragemComposta(numero_cartas):
    cartas_aleatorias = random.sample(arcanosMaiores, numero_cartas)
    return cartas_aleatorias
total_posicoes = 7
cartas_por_posicao = [3, 1, 3]

tiragem = []

def templo():
    for numero_cartas in cartas_por_posicao:
        resultado_tiragem = tiragemComposta(numero_cartas)
        tiragem.extend(resultado_tiragem)
        print(tiragem)

templo()
