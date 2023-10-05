
from classes import *
from lista_cartoes import *
from lista_clientes import *


def inicializa_cartoes():
    criar_cartoes(20)

def entrada():
    """Instancia um Cliente e associa a um cartão.
    Armazena o cliente em uma lista enquanto estiver consumindo.
    """
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


#"função inicializa_menu utilizando arquivo JSON"
# def inicializa_menu():
#    """Esta função utiliza o arquivo arqmenu.json para
#    criar o cardápio com os itens.
#    A função lê o arquivo JSON, instancia um cardápio, popula o cardápio e retorna um cardápio pronto.
#    """
#    import json
#    arquivo = open("itens_cardapio.json", "r")
#    dic_temp = json.load(arquivo)
#    arquivo.close()
#    cardapio = Cardapio()
#    popular_cardapio(cardapio, list(dic_temp.keys()), list(dic_temp.values()))
#    return cardapio

"função inicializa_menu utilizando arquivo TXT"

def inicializa_menu():
    """Esta função utiliza o arquivo itens_menu.txt para
    criar o cardápio com os itens.
    A função lê o arquivo texto, instancia um cardápio, popula o cardápio e retorna um cardápio pronto.
    """
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
    3- Finalizar a Comanda 
    4- Gerenciar Menu
    """
# OBS. Fazer o Cancelar Pedido


def menu_principal():
    cardapio = inicializa_menu()    # cria o cardápio
    inicializa_cartoes()            # cria uma lista de cartões
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
            finalizar_comanda()


if __name__ == "__main__":
    menu_principal()

