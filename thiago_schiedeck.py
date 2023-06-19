#Thiago Schiedeck Dias da Silveira

listaA = []
listaB = []

def menu():
    print("1 - Inserir Cadeiras")
    print("2 - Listar Cadeiras")
    print("3 - Posição das Cadeiras")
    print("4 - Inserir Números")
    print("5 - Listar Números")
    print("6 - Converter Números")
    print("10 - FIM")
    print("")
    print("Escolha Uma Opção:")
    
def inserecadeira():
    print("")
    cadeiras = input("Digite a cadeira: ")
    listaA.append(cadeiras.upper())
    print("")
    continuar = input("Deseja continuar (S/N)? ")
    while continuar.upper() == "S":
        print("")
        cadeiras = input("Digite a cadeira: ")
        listaA.append(cadeiras.upper())
        print("")
        continuar = input("Deseja continuar (S/N)? ")
        
def listarcadeiras():
    print("")
    print ("Suas cadeiras são:")
    for i in listaA:
        print(f"{i[0:3]}")
    print("")
    
def posicaocadeira():
    print("")
    listaAtamanhos = []
    for i in range(len(listaA)):
        tamanho = len(listaA[i])
        listaAtamanhos.append(tamanho)
    sort_index = []
    for x in listaAtamanhos:
        sort_index.append(x)
    sort_index.sort(reverse=True)
    cadeira = input("Digite o nome da cadeira que você quer saber:")
    cadeira_maiusc = cadeira.upper()
    posicao0 = listaA.index(cadeira_maiusc)
    posicao1 = listaAtamanhos[posicao0]
    posicao_final = sort_index.index(posicao1)
    print("")
    print(f"""A cadeira de {cadeira} é a {posicao_final+1}ª com maior número de caracteres.""")
    print("")
    
def inserenumeros():
    print("")
    for i in range (10):
        numeros = int(input(f"Digite o {i+1}º número inteiro entre 100 e 500: "))
        if numeros >= 100 and numeros <= 500:
            listaB.append(numeros)
            continue
        else:
            print("")
            print("Ops, parece que o número que você digitou não está entre 100 e 500. :(")
            break
        
def listarnumeros():
    print("")
    print("Os números digitados foram: ")
    for i in listaB:
        print(i)
    multiplos = []
    for x in range (len(listaB)):
        resultado = listaB[x] % 10
        if resultado == 0:
            multiplos.append(listaB[x])
        else:
            continue
    print("")
    print("Entre estes, terminam em 0:")
    for y in multiplos:
        print(y)
        print("")
        
def conversao():
    print("")
    indice = int(input("Digite o índice do número que você deseja converter:"))
    listaB[indice] = str(listaB[indice])
    print("")
    print(f"Pronto, o valor {listaB[indice]} foi transformado em uma string.")
    print("")
        
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
    elif opcao == 5:
        listarnumeros() 
    elif opcao == 6:
        conversao() 
    
    
