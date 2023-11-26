import random

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

while True:
    print('==============================================')
    print('=====|Bem vindo ao Oráculo Mikrokosmos|=======')
    print('==============================================')

    print('Selecione o tipo de tiragem: ')
    print('1 - Tiragem única')
    print('2 - Tiragem Multipla')
    print('3 - Sair')

    intencoes = {}

    def tiragemUnica():
        carta_aleatoria = random.choice(arcanosMaiores)
        return carta_aleatoria

    def tiragemComposta(numero_cartas):
        cartas_aleatorias = random.sample(arcanosMaiores, numero_cartas)
        return cartas_aleatorias

    tiragem = int(input())

    if tiragem == 1:
        intencao = input('Digite a pergunta do consulente: ')
        resultado_tiragem = tiragemUnica()
        print(resultado_tiragem)
        intencoes[intencao] = resultado_tiragem

    elif tiragem == 2:
        intencao = input('Digite a pergunta do consulente: ')
        print('Digite o número de cartas a serem tiradas: ')
        numero_cartas = int(input())
        resultado_tiragem = tiragemComposta(numero_cartas)
        print(resultado_tiragem)
        intencoes[intencao] = resultado_tiragem

    else:
        print('Obrigado pela consulta')
        break

print("Dicionário de Intenções:", intencoes)
