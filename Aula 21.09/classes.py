class Cardapio:
    def __init__(self):
        self.itens = []
        self.preco = []
        
    def inserir_item(self, produto, preco):
        self.itens.append(produto)
        self.preco.append(preco)
        
    def retirar_item(self, produto):
        index = self.itens.index(produto)
        self.itens.remove(produto)
        self.preco.pop(index)
        
    def menu_itens(self):
        for i in range(len(self.itens)):
            print(f" {str(self.itens[i]).ljust(45,'.')}...{self.preco[i]}")
        item_escolhido = int(input("Escolher opção: "))
        return self.itens[item_escolhido], self.preco[item_escolhido]

class Pedido:
    def __init__(self):
        self.item = None
        self.quantidade = 0
        self.valor = 0

    def escolher_item(self, cardapio):
        item, preco = cardapio.menu_itens()
        qt_item = int(input(f"Quantidade: "))
        valor = qt_item * float(preco)
        print(f"""
        Confirmando:
        - {item} - {preco} Qt: {qt_item} = {valor} """)
        confirma = input("Confirma (S/N): ").upper()

        if confirma == "S":
            self.item = item #escolha[0]
            self.quantidade = qt_item
            self.valor = valor

class Cartao:
    def __init__(self):
        self.numero = None
        self.itens_consumo = []
        self.ativo = False

    def ativar_cartao(self):
        pass

    def desativar(self):
        pass

    def adicionar_pedido(self, pedido):
        self.itens_consumo.append(pedido)

    def conferir_itens(self):
        print("Consumo: ")
        soma = 0
        for consumo in self.itens_consumo:
            print(f"""
            - {consumo}""")
