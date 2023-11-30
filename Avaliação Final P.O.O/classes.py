class Tarefa:
    def __init__(self, titulo, descricao, status, criacao, conclusao):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__status = status
        self.__criacao = criacao
        self.__conclusao = conclusao
        
    def atualizar_descricao(self, descricao):    
        self.__descricao = descricao
        
    def iniciar_tarefa(self):
        self.__status = "Em andamento"
        
    def concluir_tarefa(self):
        self.__status = "Concluída"
    
class Usuario:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
        self.__tarefas = []
        self.adm = None
        
    def 