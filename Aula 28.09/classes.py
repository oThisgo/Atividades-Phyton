class Cardapio:
    def __init__(self):
        self.itens = []
        self.precos = []

    def inserir_itens(self, item, preco):
        self.itens.append(item)
        self.precos.append(preco)

    def print_itens(self):
        print("\n"*30)
        print("="*30)
        print("Cardápio: ")
        for ind, item in enumerate(self.itens):
            print(f"  {str(item).ljust(45,'.')}...{self.precos[ind]}")

    def menu_itens(self):
        print("\n"*30)
        print("="*30)
        print("Cardápio: ")
        for ind, item in enumerate(self.itens):
            print(f"{ind+1}- {str(item).ljust(45,'.')}...{self.precos[ind]}")

        item_escolhido = int(input(f"Escolher opção [1-{len(self.itens)}]: ")) - 1
        return self.itens[item_escolhido], self.precos[item_escolhido]

class Pedido:
    def __init__(self):
        self.item = None
        self.quantidade = 0
        self.valor_pedido = 0

    def escolher_item(self, cardapio):
        item, preco = cardapio.menu_itens()
        qt_item = int(input(f"  Quantidade: "))
        valor_pedido = qt_item * float(preco)
        print(f"""
        Confirmando:
           - {item} - {preco} Qt: {qt_item} = {valor_pedido} """)
        confirmado = input("Confirma s/n: ").upper()

        if confirmado == "S":
            self.item = item
            self.quantidade = qt_item
            self.valor_pedido = valor_pedido






#
# class Cartao:
#     def __init__(self):
#         self.numero = None
#         self.itens_consumo = list()
#         self.ativo = False
#
#
#     def ativar_cartao(self):
#         pass
#
#     def desativar_cartao(self):
#         pass
#
#     def adicionar_pedido(self, pedido):
#         self.itens_consumo.append(pedido)
#
#     def conferir_itens(self):
#         print("\nConsumo:")
#         soma = 0
#         for pedido in self.itens_consumo:
#             print(f"> {pedido.item} {pedido.quantidade} {pedido.valor_pedido}")
#             soma += pedido.valor_pedido
#
#
#         print(f">>> Total: {soma}")

""" """



### Atualização da Classe Cartão
class Cartao:
    numero_atual = 100

    def __init__(self):
        # self.numero = None
        self.numero = Cartao.numero_atual
        self.itens_consumo = list()
        self.ativo = True
        Cartao.numero_atual += 1

    def is_ativo(self):
        return self.ativo

    def ativar_cartao(self):
        self.ativo = True

    def desativar_cartao(self):
        self.ativo = False

    def adicionar_pedido(self, pedido):
        self.itens_consumo.append(pedido)

    def conferir_itens(self):
        print("\nConsumo:")
        soma = 0
        for item in self.itens_consumo:
            print(f"> {item.item} {item.quantidade} {item.valor_pedido}")
            soma += item.valor_pedido

        print(f">>> Total: {soma}")

class Cliente:
    num = 1

    def __init__(self):
        self.nome = None
        self.telefone = None
        self.cartao = None
        Cliente.num += 1

    def atribuir_cartao(self, num_cartao):
        self.cartao = num_cartao

print(__name__)

if __name__ == "__main__":
    print("Arquivo de classes")


# c1 = Cartao()
# print(c1.numero, c1.numero_atual)
# c2 = Cartao()
# print(c2.numero, c2.numero_atual)
# print(c1.numero, c1.numero_atual, Cartao.numero_atual)


