class Porta:
    def __init__(self, altura, largura, cor):
        self.__altura = 0
        self.__largura = 0
        self.__cor = ''
        self.__aberta = None
        self.__fechadura = None
    
    def __str__(self):
        return f"""
            Altura: {self.__altura} Largura: {self.__largura}
            Cor: {self.__cor} Aberta: {self.__aberta}
            Fechadura: {self.__fechadura}
        """
        
    def abrir(self):
        self.__aberta = True
            
    def fechar(self):
        self.__aberta = False
        
    def instalar_fechadura(self, fechadura):
        self.__fechadura = fechadura
        
class Fechadura:
    def __init__(self, chave):
        self.__senha = chave
        self.__estado = None
    
    def trancada(self):
        self.__estado = True
        
    def destrancada():
        self.__estado = False
    
    def __str__(self):
        return f"""Segredo: {self.__senha} Trancada: {self.__estado}"""
    
fechadura = Fechadura('13579')
fechadura2 = Fechadura('54321')
fechadura3 = Fechadura('12345')
porta = Porta(2.10, 0.80, "Branca")
porta2 = Porta(2.10, 0.80, "Marrom")
porta3 = Porta(2.10, 0.80, "Transparente")

porta.instalar_fechadura(fechadura)
porta.abrir()
print(porta)

