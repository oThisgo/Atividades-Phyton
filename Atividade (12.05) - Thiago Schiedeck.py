cidades = []
populacao = []
cidade = input("Digite o nome da cidade: ")
cidades.append(cidade)
habitantes = int(input("Digite o número de habitantes: "))
populacao.append(habitantes)
continuar = input("Deseja continuar (S/N)?")
while continuar.upper() == "S":
    cidade = input("Digite o nome da cidade: ")
    cidades.append(cidade)
    habitantes = int(input("Digite o número de habitantes: "))
    populacao.append(habitantes)
    continuar = input("Deseja continuar (S/N)?")
print("Lista de cidades:")
for i in range (len(cidades)):
    print(cidades[i], populacao[i])
media = sum(populacao)/len(cidades)
maior = populacao.index(max(populacao))
menor = populacao.index(min(populacao))
print("")
print("A cidade com maior população é" , cidades[maior] , "e a menor" , cidades[menor] , "que possuem uma população de" , max(populacao) , "e" , min(populacao) , "respectivamente. Já a média da população de todas as cidades é" , media , ".")
    
    
    