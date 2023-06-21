#Thiago Schiedeck Dias da Silveira

lst_nome = []
lst_idade = []
lst_peso = []
lst_altura = []
IMC = []

def menu():
    print("1 - Inserir alunos")
    print("2 - Listar todos os alunos")
    print("3 - Listar os dados de um aluno")
    print("4 - Filtrar os alunos por idade")
    print("5 - Excluir um aluno")
    print("9 - FIM")
    print("")
    
def inserealuno():
    nome = input("Digite o nome do aluno (para encerrar não digite nada):")
    while nome != '':
        lst_nome.append(nome.upper())
        idade = int(input("Digite a idade do aluno: "))
        lst_idade.append(idade)
        peso = float(input("Digite o peso do aluno (Kg): "))
        lst_peso.append(peso)
        altura = float(input("Digite a altura do aluno (m): "))
        lst_altura.append(altura)
        imc = peso / (altura * altura)
        IMC.append(imc)
        nome = input("Digite o nome do aluno (para encerrar não digite nada):")
        
def listatodos():
    print("")
    print("Lista de alunos:")
    for i in range (len(lst_nome)):
        print(f"""
        NOME: {lst_nome[i]} IDADE: {lst_idade[i]} anos PESO: {lst_peso[i]}kg ALTURA: {lst_altura[i]}m IMC: {IMC[i]}kg/m²""")
    imc_medio = sum(IMC) / len(IMC)
    print("")
    print(f"IMC MÉDIO: {imc_medio}")
    print("")
    
def listasolo():
    aluno = input("Digite o nome completo do aluno que você procura: ")
    alunomaiusc = aluno.upper()
    indice = lst_nome.index(alunomaiusc)
    print("")
    print(f"""Aqui está:
    NOME: {lst_nome[indice]} IDADE: {lst_idade[indice]} anos PESO: {lst_peso[indice]}kg ALTURA: {lst_altura[indice]}m IMC: {IMC[indice]}kg/m²
    """)
    
def filtraidade():
    IMC_grupo = []
    age = int(input("Digite a idade que você procura:"))
    print("")
    print(f"Aqui estão todos os alunos com {age} anos:")
    for i in range (len(lst_idade)):
        if lst_idade[i] == age:
            print(f"""
            NOME: {lst_nome[i]} IDADE: {lst_idade[i]} anos PESO: {lst_peso[i]}kg ALTURA: {lst_altura[i]}m IMC: {IMC[i]}kg/m²""")
            IMC_grupo.append(IMC[i])
        else:
            continue
    print("")
    print(f"IMC MÉDIO: {sum(IMC_grupo) / len(IMC_grupo)}")
    print("")
        
def excluialuno():
    excluido = input("Digite o nome do aluno que deseja remover:")
    excluidomaiusc = excluido.upper()
    indiceB = lst_nome.index(excluidomaiusc)
    del lst_nome[indiceB]
    del lst_altura[indiceB]
    del lst_idade[indiceB]
    del lst_peso[indiceB]
    del IMC[indiceB]
    print("")
    print(f"Pronto, aluno {excluidomaiusc} deletado.")
    print("")
    
while True:
    menu()
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        inserealuno()
    elif opcao == 2:
        listatodos()
    elif opcao == 3:
        listasolo()
    elif opcao == 4:
        filtraidade()
    elif opcao == 5:
        excluialuno()
    elif opcao == 9:
        break