#Thiago Schiedeck Dias da Silveira

listaA = []
listaB = []

def menu():
    print("1 - Inserir Cadeiras")
    print("2 - Listar Cadeiras")
    print("3 - Posição das Cadeiras")
    print("4 - Inserir Números")
    print("4 - Listar Números")
    print("10 - FIM")
    print("")
    print("Escolha Uma Opção:")
    
def inserecadeira():
    cadeiras = input("Digite a cadeira: ")
    listaA.append(cadeiras.upper())
    continuar = input("Deseja continuar (S/N)? ")
    while continuar.upper() == "S":
        cadeiras = input("Digite a cadeira: ")
        listaA.append(cadeiras.upper())
        continuar = input("Deseja continuar (S/N)? ")
        
def listarcadeiras():
    print ("Suas cadeiras são:")
    for i in listaA:
        print(i)

def posicaocadeira():
    listaAtamanhos = []
    for i in range (len(listaA)):
        tamanho = len(listaA[i])
        listaAtamanhos.insert(i, tamanho)
        listaAtamanhos.sort(reverse=True)
    cadeira = input("Digite o nome da cadeira que você quer saber:")
    cadeira_maiusc = cadeira.upper()
    posicao_original = listaA.index(cadeira_maiusc)
    print(f"""A cadeira de {cadeira} é a {listaAtamanhos.index(posicao_original)}ª com maior número de caracteres.""")
    
def inserenumeros():
    for i in range (10):
        numeros = int(input(f"Digite o {i}º número inteiro entre 100 e 500: "))
        if numeros >= 100 and numeros <= 500:
            listaB.append(numeros)
            continue
        else:
            print("Ops, parece que o número que você digitou não está entre 100 e 500. :(")
            break
        
while True:
    menu()
    opcao=int(input())
    if opcao==10:
        print("FIM")
        break
    elif opcao == 1:
        inserecadeira()
    elif opcao == 2:
        listarcadeiras()
    elif opcao == 3:
        posicaocadeira()
    elif opcao == 4:
        inserenumeros()

        