menu = f"""
0 - Exit
1 - Cadastrar cliente
2 - Realizar um pedido
3 - Finalizar a comanda
"""

def Entrada():
    pass

def Consumo():
    pass

def Concluir():
    pass

while True:
    print(menu)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        Entrada()
    elif opcao == 2:
        Consumo()
    elif opcao == 3:
        Concluir()
    elif opcao == 0:
        break
