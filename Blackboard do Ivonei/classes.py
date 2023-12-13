from datetime import datetime

#objeto Tarefa
class Tarefa:
    
    def __init__(self, titulo, descricao, data_criacao = '',   data_conclusao = ''):
        self._titulo =  titulo
        self._descricao = descricao
        self._status_tarefa = False
        self._data_criacao = data_criacao
        self._data_conclusao =  data_conclusao
  
    @property #retorna o valor do atributo
    def titulo(self):
      return self._titulo.title()
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def status_tarefa(self):
        return self._status
    
    @property
    def data_conclusao(self):
        return self._data_conclusao
    
    @property
    def data_criacao(self):
        return self._data_criacao
    
    @titulo.setter #uso do setter para definir um valor para o atributo
    def titulo(self, titulo):
        self._titulo = titulo
      
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
    
    @status_tarefa.setter
    def status_tarefa(self, status_tarefa):
        self._status_tarefa = status_tarefa
    
    @data_criacao.setter
    def data_criacao(self, data_criacao):
        self._data_criacao = data_criacao
        
    @data_conclusao.setter
    def data_conclusao(self, data_conclusao):
        self._data_conclusao = data_conclusao
      
    def return_status(self):
        if self._status_tarefa is True:
            return 'Concluida'
        else:
            return 'Nao concluida'
    
    # formata a data no formato dd/mm/aaaa
    def format_data_criacao(self): 
        if self._data_criacao != '':
            dia = self._data_criacao[0:2]
            mes = self._data_criacao[2:4]
            ano = self._data_criacao[4:]
            
            return f'{dia}/{mes}/{ano}'
        else:
            return 'Sem data...'
    
    def format_data_conclusao(self):
        if self._data_conclusao != '':
            dia = self._data_conclusao[0:2]
            mes = self._data_conclusao[2:4]
            ano = self._data_conclusao[4:]
            
            return f'{dia}/{mes}/{ano}'
        else:
            return 'Sem data...'
    
    def __str__(self):
        return f"""
        Título: {self._titulo}
        Descrição: {self._descricao}
        Criada em: {self.format_data_criacao()} Concluída em: {self.format_data_criacao()}
        Status: {self.return_status()}"""
    
    def create_dict(self): #cria um dicionario para a tarefa
        status = 'Concluida' if self._status_tarefa is True else 'Nao concluida'
        return {
        'Titulo': self._titulo,
        'Descricao': self._descricao,
        'Criacao': self.format_data_criacao(), 
        'Conclusao': self.format_data_criacao(),
        'Status': self.return_status()}
        
    def update_status(self): #muda o status e adiciona a data da conclusao
        if self._status_tarefa is False:
            self._status_tarefa = True
            hoje = datetime.now()
            dia = hoje.day if len(f'{hoje.day}') == 2 else f'0{hoje.day}'
            self._data_conclusao = f'{dia}{hoje.month}{hoje.year}'
            print(f"""
            Tarefa: {self._titulo} - Concluida em: {self.format_data_conclusao()} 
            """)
        else:
            self._status_tarefa = False
            self._data_conclusao = 'Sem data...'
            print(f"""
            Tarefa: {self.__titulo} - Nao concluida
            """)
    
    #funções para alterar os atributos
    def update_title(self, titulo):
        self._titulo = titulo
        print("Titulo alterado com sucesso!")
      
    def update_desc(self, descricao): 
        self._descricao = descricao
        print("Descrição alterada com sucesso!")
    
    def update_data_conclusao(self, data_conclusao):
        self._data_conclusao = data_conclusao
        print("Data de conclusão alterada com sucesso")
    
    def update_data_criacao(self, data_criacao):
        self._data_criacao = data_criacao
        print("Data de Criação alterada com sucesso")
      
    def upload_data_criacao(self, data_criacao): #carrega a data através do json
        if data_criacao == 'Sem data...':
            self._data_criacao = ''
        else:
            data = data_criacao.split('/')
            self._data_criacao = data[0] + data[1] + data[2]
            
    def upload_data_conclusao(self, data_conclusao):
        if data_conclusao == 'Sem data...':
            self._data_conclusao = ''
        else:
            data = data_conclusao.split('/')
            self._data_conclusao = data[0] + data[1] + data[2]
        
    def upload_status(self, status): #carrega o status através do json
        self._status_tarefa = status == 'Concluida'
      
#objeto Projeto
class Projeto(Tarefa): #uso de herança para herdar os metodos do objeto tarefa
    def __init__(self, titulo, descricao, data_criacao = '', data_conclusao = ''):
        super().__init__(titulo, descricao, data_criacao, data_conclusao) #super() "instancia" a tarefa dentro do projeto
        self._tarefas_projeto = []

    @property
    def tarefas_projeto(self):
        return self._tarefas_projeto
    
    @tarefas_projeto.setter
    def tarefas_projeto(self, tarefa):
        self._tarefas_projeto.append(tarefa)
    
    def atribuir_tarefa(self, tarefa): #anexa a tarefa ao respectivo projeto
        print(f"{tarefa._titulo} atribuida com sucesso a {self._titulo}")
        return self._tarefas_projeto.append(tarefa)    
    
    def show_tasks_project(self): #retorna as tarefas do respectivo projeto
        print({self._titulo})
        
        if len(self._tarefas_projeto) == 0:
            print('O projeto não possui tarefas.')
        else:
            num = 0
            
            for tarefa in self._tarefas_projeto:
                num += 1
            print(f'Tarefa {num} - {str(tarefa)}')
        
    def exclude_project_task(self, num):
        print(f'Tarefa {self._tarefas_projeto[num].titulo} excluída')
        return self._tarefas_projeto.pop(num) 

    def finish_task_project(self): #conclui a tarefa especificada
        if len(self._tarefas_projeto) == 0:
            print(f'O projeto não possui tarefas.')
        else:
            self.show_tasks_project()
            task_num = int(input('\nDigite o número da tarefa concluída: ')) - 1
            
        if task_num < len(self.__tarefas_projeto):
            self._tarefas_projeto[task_num].update_status()
        else:
            print('Digite um número válido!')
  
    def update_project_status(self): #atualiza o status do projeto como concluído e atribui a data de conclusão
        if self._status is False:
            self._status = True
            hoje = datetime.now()
            dia = hoje.day if len(f'{hoje.day}') == 2 else f'0{hoje.day}'
            self._data_conclusao = f'{dia}{hoje.month}{hoje.year}'
            print(f"""
            Projeto: {self._titulo} - Concluído em: {self.format_data_conclusao()} 
            """)
        else:
            self._status = False
            self._data_conclusao = 'Sem data...'
            print(f"""
            Projeto: {self._titulo} - Não concluído
            """)
            
#objeto Usuário
class Usuario:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._tarefas = []
  
    @property
    def nome(self):
        return self._nome
  
    @property
    def email(self):
        return self._email
  
    @property
    def tarefas(self):
        return self._tarefas

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @email.setter
    def email(self, email):
        self._email = email
     
    @tarefas.setter
    def tarefas(self, tarefas):
        self._tarefas.append(tarefas)
  
    def __str__(self):
        return f"""
        Nome: {self._nome}
        E-Mail: {self._email}
        Nº de Tarefas: {len(self._tarefas)}
        """
  
    def exclude_user_task(self, num):
        print(f'Tarefa {self._tarefas[num].titulo} excluída')
        return self._tarefas.pop(num) 

    def create_dict(self): #cria um dicionario para o usuario
        return {
        'Nome': self._nome, 
        'Email': self._email }
  
    def show_tasks_user(self): #lista as tarefas atribuidas ao usuario
        print({self._nome})
    
        if len(self._tarefas) == 0:
            print('O usuário não possui tarefas.')
        else:
            num = 0
            
            for tarefa in self._tarefas:
                num += 1
            print(f'Tarefa {num} - {str(tarefa)}')
  
    def atribuir_tarefa(self, tarefa): #atribui tarefas ao usuário
        self._tarefas.append(tarefa)
        print(f"{tarefa._titulo} atribuida a {self._nome}")
        
    def finish_task_user(self): #marca a tarefa como concluída para o usuário
        if len(self._tarefas) == 0:
            print('O usuário não possui tarefas')
        else:
            self.show_tasks_user()
            task_num = int(input('\nDigite o número da tarefa concluída:')) - 1
            
        if task_num < len(self.tarefas):
            self._tarefas[task_num].update_status()
        else:
            print('Digite um número válido!')