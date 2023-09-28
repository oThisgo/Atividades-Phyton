import random
from classes import Cartao


lista_cartoes = list()

def adicionar_cartao(cartao):
    lista_cartoes.append(cartao)

def criar_cartoes(qt_cartoes):
    for qt in range(qt_cartoes):
        adicionar_cartao(Cartao())

def menu_cartoes():
    print("\nCartões:")
    ind = 0
    for cartao in lista_cartoes:
        if cartao.is_ativo():
            ind += 1
            print(f"  {ind} - {cartao.numero}")


    escolha = int(input(f"   Escolha 1-{ind}: ")) - 1
    return lista_cartoes[escolha]

def seleciona_cartao():
    random.randrange(min(lista_cartoes), len(lista_cartoes))



