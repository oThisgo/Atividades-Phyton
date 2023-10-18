from classes import Cartao

lista_de_cartoes = list()

def adicionar_cartao(cartao):
    lista_de_cartoes.append(cartao)

def criar_cartoes(qt_cartoes):
    for qt in range(qt_cartoes):
        adicionar_cartao(Cartao())

def get_cartao():
    for cartao in lista_de_cartoes:
        if not cartao.is_ativo():
            cartao.ativar_cartao()
            return cartao
    input("Não há cartões disponíveis. Enter")
    return None

def menu_cartoes():
    print("\nCartões:")
    ind = 0
    for cartao in lista_de_cartoes:
        if cartao.is_ativo():
            ind += 1
            print(f"  {ind} - {cartao.numero}")

    escolha = int(input(f"   Escolha 1-{ind}: ")) - 1
    return lista_de_cartoes[escolha]

def liberar_cartao(cartao):
    for c in lista_de_cartoes:
        if c == cartao:
            cartao.itens_consumo.clear()
            cartao.desativar_cartao()
            input("Cartão liberado e desativado. ")
