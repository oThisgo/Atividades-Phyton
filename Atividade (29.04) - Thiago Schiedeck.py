valor = float(input("Digite um valor: "))
print("")
while valor != 0:
    print("! TABUADA DO", valor , "!") 
    for i in range (1,11,1):
        resultado = valor * i
        print(valor , "x" , i , "=" , resultado)
    print("")
    valor = float(input("Digite outro valor: "))
print("-- Programa Encerrado --")
    