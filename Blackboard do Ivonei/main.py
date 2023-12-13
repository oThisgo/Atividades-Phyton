from listas import *
from classes import *

#Thiago Schiedeck Dias da Silveira

def cadastro(): #cadastrar usuário e adicionar a lista
  print("Cadastrar\n")
    
  nome = str(input('NOME: '))
  email = str(input('E-MAIL: '))
    
  print(f'Usuário cadastrado com sucesso!')
  return lista_usuarios.append(Usuario(nome, email))
    
def criar_projeto(): #criar um projeto e adicionar a lista
  print("Criar um Projeto\n")
    
  nome = str(input('Nome: '))
  descricao = str(input('Descrição: '))
  data_criacao = str(input('Criação: '))
  data_conclusao = str(input('Conclusão: '))   
    
  print(f'Projeto criado com sucesso!')  
  return lista_projetos.append(Projeto(nome, descricao, data_criacao, data_conclusao))

def criar_tarefa(): 
  print("Criar uma Tarefa\n")

  nome = str(input('Nome: '))
  descricao = str(input('Descrição: '))
  data_criacao = str(input('Criação: '))
  data_conclusao = str(input('Conclusão: ')) 
  
  return Tarefa(nome, descricao, data_criacao, data_conclusao)
  
  
def acrescentar_tarefa(tarefa): #acrescenta a tarefa a um usuário e/ou projeto
  send_to_p = input('Atribuir essa tarefa a um projeto (s/n)? ').strip()[0].upper()
  if send_to_p == 'S':
    list_p()
    project_num = int(input('\nEscolha o projeto que deve receber a tarefa: ')) - 1
    lista_projetos[project_num].atribuir_tarefa(tarefa)
  else:
    send_to_u = input('Atribuir essa tarefa a um usuário (s/n)? ').strip()[0].upper()
    if send_to_u == 'S':
      list_u()
      user_num = int(input('\nEscolha o usuário que deve receber a tarefa: ')) - 1
      lista_usuarios[user_num].atribuir_tarefa(tarefa)
 
def list_p(): #listar os projetos 
  if len(lista_projetos) == 0:
    print('Não há nenhum projeto ainda.')
  else:
    num = 0
    for projeto in lista_projetos:
      num += 1
      print(f'Projeto {num} - {str(projeto)} ') 
      
def list_u(): #listar os usuarios
  if len(lista_usuarios) == 0:
    print('Não há nenhum usuário ainda.')
  else:
    num = 0
    for usuario in lista_usuarios:
      num += 1
      print(f'Usuário {num} - {str(usuario)} ')
      
def conclude_task_user(): #define a tarefa como concluida para o usuario
  list_u()
  user_num =  int(input('\nA tarefa deve ser concluída para qual usuário? ')) - 1
  lista_usuarios[user_num].finish_task_user()
  
def conclude_task_project(): #define a tarefa como concluida para o projeto
  list_p()
  project_num =  int(input('\nA tarefa deve ser concluída para qual projeto? ')) - 1
  lista_projetos[project_num].finish_task_project()

def users_tasks(): #lista as tarefas de um usuário específico
  list_u()
  user_num =  int(input('\nListar as tarefas de qual usuário? ')) - 1
  lista_usuarios[user_num].show_tasks_user()
  
def projects_tasks(): #lista as tarefas de um projeto específico
  list_p()
  project_num =  int(input('\nListar as tarefas de qual projeto? ')) - 1
  lista_projetos[project_num].show_tasks_project()

def delete_user_task():
  list_u()
  user_num =  int(input('\nListar as tarefas de qual usuário? ')) - 1
  lista_usuarios[user_num].show_tasks_user()
  task_num = int(input('Digite a tarefa que você deseja excluir: ')) - 1
  lista_usuarios[user_num].exclude_user_task(task_num)

def delete_project_task():
  list_p()
  project_num =  int(input('\nListar as tarefas de qual projeto? ')) - 1
  lista_projetos[project_num].show_tasks_project()
  task_num = int(input('Digite a tarefa que você deseja excluir: ')) - 1
  lista_projetos[project_num].exclude_project_task(task_num)
  

menu = """

  Blackboard do Ivonei

  1 - Cadastrar usuário
  2 - Criar projeto
  3 - Criar tarefa
  4 - Concluir uma tarefa do usuário
  5 - Concluir uma tarefa do projeto
  6 - Listar todos usuarios cadastrados
  7 - Listar todos projetos cadastrados 
  8 - Mostrar tarefas de usuários
  9 - Mostrar rarefas de projetos
  10 - Excluir tarefa de usuário
  11 - Excluir tarefa de projeto
  0 - Sair

"""

def menu_principal():
  load()            
  while True:
    print('-'*20)
    escolha = input(menu + "Escolha: ")
    if escolha == "1":
      cadastro()
    elif escolha == "2":
      criar_projeto()
    elif escolha == "3":
      acrescentar_tarefa(criar_tarefa())
    elif escolha == "4":
      conclude_task_user()
    elif escolha == "5":
      conclude_task_project()
    elif escolha == "6":
      list_u()
    elif escolha == "7":
      list_p()
    elif escolha == "8":
      users_tasks()
    elif escolha == "9":
      projects_tasks()
    elif escolha == "10":
      delete_user_task()
    elif escolha == "11":
      delete_project_task()
    elif escolha == "0":
      save()
      break
     
if __name__ == "__main__":
  menu_principal()