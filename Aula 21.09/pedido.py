from classes import *
from dados_iniciais import *

cardapio = Cardapio()
popular_lista(
    cardapio,
    aux_itens.split(";\n"),
    aux_precos.split("\n")
)

cartao = Cartao()

pedido = Pedido()
pedido.escolher_item(cardapio)
cartao.adicionar_pedido(pedido)
cartao.conferir_itens()
