class Porta:
    def __init__(self, altura, largura):
        self.__altura = altura
        self.__largura = largura
        self.__cor = None
        self.__aberta = None
        self.__fechadura = None

    def instalar_fechadura(self, fechadura, chave):
        self.__fechadura = fechadura      # Instalo a fechadura e
        self.__aberta = True              # Deixa a porta aberta
        self.__fechadura.deschavear(chave)# Dexia a porta deschaveada

    def __sts_porta(self):
        if self.__aberta:
            return "SIM"
        return "NÃO"

    def __str__(self):
        return f"""
        Altura: {self.__altura} - Largura: {self.__largura}
        Cor: {self.__cor} - Aberta: {self.__sts_porta()} -
        Fechadura: {self.__fechadura}"""

    def abrir(self):
        if not self.__porta_is_aberta():                    # se porta está fechada
            if not self.__fechadura.fechadura_is_chaveada():# se fechadura está deschaveada
                self.__aberta = True                        # Abrir a porta
                print("Porta foi aberta...")
            else:
                print("Porta está trancada....")

    def fechar(self):
        if self.__porta_is_aberta():                          # se porta está aberta
            if not self.__fechadura.fechadura_is_chaveada():# se a fechadura está deschaveada
                self.__aberta = False                       # Fecha a porta
                print("Porta foi fechada...")
            else:
                print("Porta está trancada....")

    def __porta_is_aberta(self):
        if self.__aberta == True:
            return True
        return False

    def trancar(self, chave):
        self.__fechadura.chavear(chave)

    def destrancar(self, chave):
        self.__fechadura.deschavear(chave)

class Fechadura:
    def __init__(self, chave):
        self.__segredo = chave
        self.__chaveada = None

    def chavear(self, chave):
        if self.__segredo == chave:
            self.__chaveada = True

    def deschavear(self, chave):
        if self.__segredo == chave:
            self.__chaveada = False

    def __sts_chaveada(self):
        if self.__chaveada:
            return "CHAVEADA"
        return "DESCHAVEADA"

    def __str__(self):
        return f"""-{self.__segredo} - {self.__sts_chaveada()}"""

    # def validar_chave(self, chave):
    #     return self.__segredo == chave

    def fechadura_is_chaveada(self):
        if self.__chaveada == True:
            return True
        return False

######################
chave = "12345"
fechadura = Fechadura(chave)
print(fechadura)

porta = Porta(210, 100)
porta.instalar_fechadura(fechadura)

porta.fechar()
porta.trancar(chave)
porta.destrancar(chave)
porta.abrir()

print(porta)