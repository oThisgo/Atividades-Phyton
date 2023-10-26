class Garrafa:
    def __init__(self, volume, circunferencia):
        self.__volume = volume
        self.__circunferencia = circunferencia
        self.__cor = None
        self.__aberta = None
        self.__tampa = None
        
    def definir_tampa(self, tampa, circunferencia):
        self.__tampa = tampa
        self.__aberta = False
        self.__tampa.tampar(circunferencia)
        
    def __status_garrafa(self):
        if self.__aberta:
            return "Sim"
        return "Não"
        
    def __str__(self):
        return f"""
        Volume: {self.volume} Circunferência: {self.__circunferencia}
        Cor: {self.__cor} Aberta: {self.__status_garrafa()}
        Tampa: {self.__tampa}
        """
        
    def __garrafa_aberta(self):
        if self.__aberta == True:
            return True
        return False
        
    def abrir(self):
        if not self.__garrafa_aberta():
            if not self.__tampa.__tampa_encaixada():
                self.__aberta = True
                print("A garrafa foi aberta.")
            else:
                print("A garrafa está tampada.")
    
    def fechar(self):
        if self.__garrafa_aberta():
            if not self.__tampa.__tampa_encaixada():
                self.__aberta = False
                print("A garrafa foi fechada.")
            else:
                print("A garrafa está tampada.")
    
    def tampar(self, circunferencia):
        self.__tampa.__tampar(circunferencia)
        
    def destampar(self, circunferencia):
        self.__tampa.__destampar(circunferencia)
    
class Tampa:
    def __init__(self, circunferencia):
        self.__circunferencia = circunferencia
        self.__encaixada = None
        
    def __tampar(self, circunferencia):
        if self.__circunferencia == circunferencia:
            self.__encaixada = True
            
    def __destampar(self, circunferencia):
        if self.__circunferencia == circunferencia:
            self.__encaixada = False
            
    def __tampa_encaixada(self):
        if self.__encaixada:
            return "Encaixada"
        return "Desencaixada"
        
    def __str__(self):
        return f"{self.__circunferencia} - {self.__tampa_encaixada}"
        
    def __tampa_tampada(self):
        if self.__encaixada == True:
            return True
        return False
        
tampa = Tampa(10)
garrafa = Garrafa(500, )
