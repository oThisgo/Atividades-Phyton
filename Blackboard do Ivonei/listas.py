from classes import *
import os
import json

lista_usuarios = []
lista_projetos = []

def save(): #salva os dados no arquivo json
    dados = { }
    
    usuarios = []
    for usuario in lista_usuarios:
        user = usuario.create_dict()

        tarefas = []
        for tarefa in usuario.tarefas:
            tarefas.append(tarefa.create_dict())
        user['Tarefas'] = tarefas
        usuarios.append(user)
    dados['Usuarios'] = usuarios 
    
    projetos = []
    for projeto in lista_projetos:
        project = projeto.create_dict()

        tarefas = []
        for tarefa in projeto.tarefas_projeto:
            tarefas.append(tarefa.create_dict())
        project['Tarefas'] = tarefas
        projetos.append(project)
    dados['Projetos'] = projetos
  
    objeto = json.dumps(dados, indent=2)
  
    with open("dados.json", "w") as outfile:
        outfile.write(objeto)
  
def load(): #carrega os dados no arquivo json
    if os.path.isfile("dados.json"):
        objeto = {}
        with open('dados.json', 'r') as openfile:
            objeto = json.load(openfile)
      
        for user in objeto['Usuarios']:
            usuario = Usuario(user['Nome'], user['Email'])

            for task in user['Tarefas']:
                tarefa = Tarefa(task['Titulo'], task['Descricao'])

                tarefa.upload_status(task['Status'])
                tarefa.upload_data_criacao(task['Criacao'])
                tarefa.upload_data_conclusao(task['Conclusao'])

                usuario.tarefas.append(tarefa)
            lista_usuarios.append(usuario)
      
        for project in objeto['Projetos']:
            projeto = Projeto(project['Titulo'], project['Descricao'])

            projeto.upload_status(project['Status'])
            projeto.upload_data_criacao(project['Criacao'])
            projeto.upload_data_conclusao(project['Conclusao'])

            for task in project['Tarefas']:
                tarefa = Tarefa(task['Titulo'], task['Descricao'])

                tarefa.upload_status(task['Status'])
                tarefa.upload_data_criacao(task['Criacao'])
                tarefa.upload_data_conclusao(task['Conclusao'])

                projeto._tarefas_projeto.append(tarefa)
            lista_projetos.append(projeto)