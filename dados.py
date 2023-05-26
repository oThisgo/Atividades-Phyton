import random

lst_dados = []

valor = int(input("Digite um valor:"))
for i in range(100):
    lst_dados.append(random.randint(1,6))
    
print(f"""
Lista completa:
{lst_dados}

Quantas vezes cada valor apareceu:

1: {lst_dados.count(1)} vez(es)
2: {lst_dados.count(2)} vez(es)
3: {lst_dados.count(3)} vez(es)
4: {lst_dados.count(4)} vez(es)
5: {lst_dados.count(5)} vez(es)
6: {lst_dados.count(6)} vez(es)
""")