from classes import *
from lista_cartoes import *
from lista_clientes import *

def inicializa_cartoes():
    criar_cartoes(20)

def entrada():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cartao_cli = get_cartao()
    if cartao_cli:
        cartao_cli.ativar_cartao()
        cliente = Convidado(nome, telefone, cartao_cli)
        adicionar_cliente(cliente)

def consumo(cardapio):
    while True:
        pedido = Pedido()
        pedido.escolher_item(cardapio)
        cartao_cliente = ler_cartao()
        if cartao_cliente:
            cartao_cliente.adicionar_pedido(pedido)
            if input("Escolher outro item s/n? ").upper() != "S":
                break

def cancelar_pedido():
    while True:
        cartao_cliente = ler_cartao()
        cartao_cliente.conferir_itens()
        if cartao_cliente:
            pedido = int(input("Qual pedido você deseja cancelar?"))
            cartao_cliente.remover_pedido(pedido)
            if input("Escolher outro item s/n? ").upper() != "S":
                break
        
def encerramento():
    cartao_cliente = ler_cartao()
    cartao_cliente.conferir_itens()
    if input("Confirma pagamento s/n? ").upper() == "S":
        liberar_cliente(cartao_cliente)
        liberar_cartao(cartao_cliente)
        input("OK. Pagamento Confirmado. Cartão liberado. Enter")
    else:
        input("Pagamento Cancelado. Enter")

def popular_cardapio(cardapio, lista_itens, lista_precos):
    for ind in range(len(lista_itens)):
        cardapio.inserir_itens(lista_itens[ind], lista_precos[ind])

def inicializa_menu():
    arquivo = open("itens_menu.txt", "r")
    lista_itens = []
    lista_precos = []

    for linha in arquivo:
        item, preco = linha.split(";")
        lista_itens.append(item)
        lista_precos.append(preco[:-1])

    arquivo.close()
    cardapio = Cardapio()
    popular_cardapio(cardapio, lista_itens, lista_precos)
    return cardapio

def ler_cartao():
    num_cartao = input("Digite número Cartão: ")
    return get_cartao_cliente(num_cartao)

def finalizar_comanda():
    cartao_cliente = ler_cartao()
    cartao_cliente.conferir_itens()
    if input("Confirma pagamento s/n? ").upper() == "S":
        liberar_cliente(cartao_cliente)
        liberar_cartao(cartao_cliente)
        input("OK. Pagamento Confirmado. Cartão liberado. Enter")
    else:
        input("Pagamento Cancelado. Enter")

    print(len(lista_clientes))
    for c in lista_de_cartoes:
        print("  > ",c.numero, len(c.itens_consumo))

menu = """
=========================================
    MENU - Principal
=========================================
    0- Exit
    1- Cadastrar Cliente
    2- Realizar um Pedido
    3- Cancelar um Pedido
    4- Finalizar a Comanda 
    """
    
def menu_principal():
    cardapio = inicializa_menu()    
    inicializa_cartoes()            
    while True:
        print("\n"*20)
        escolha = input(menu + "Escolha: ")
        if escolha == "0":
            break
        elif escolha == "1":
            entrada()
        elif escolha == "2":
            consumo(cardapio)
        elif escolha == "3":
            cancelar_pedido()
        elif escolha == "4":
            finalizar_comanda()

if __name__ == "__main__":
    menu_principal()