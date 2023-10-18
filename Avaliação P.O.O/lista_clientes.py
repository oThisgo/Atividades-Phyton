lista_clientes = list()

def adicionar_cliente(cliente):
    lista_clientes.append(cliente)

def get_cartao_cliente(num_cartao):
    for cliente in lista_clientes:
        if cliente.cartao.numero == int(num_cartao):
            return cliente.cartao
    input("Cartao não encontrado/Inválido. Enter")
    return None

def liberar_cliente(cartao):
    for cliente in lista_clientes:
        if cliente.cartao == cartao:
            lista_clientes.remove(cliente)
