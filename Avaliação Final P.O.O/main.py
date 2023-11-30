
p = Projeto()
#dicionario e criacao de JSON
d = {10 : "Projeto 1", 20 : "Projeto 2", 30 : "Projeto 3"}
with open("nda.json", "n") as arq:
    json.dump(d, arq)

menu = """
=========================================
    MENU - Principal
=========================================
    0- Exit
    1- Atribuir tarefa
    2- Concluir tarefa
    3- Cancelar um Pedido
    4- Finalizar a Comanda 
    """
    
menu = """
=========================================
    MENU - Principal
=========================================
    0- Exit
    1- Criar tarefa
    2- Realizar um Pedido
    3- Cancelar um Pedido
    4- Finalizar a Comanda 
    """