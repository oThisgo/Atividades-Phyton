lst_professores = []
lst_notas1 = []
lst_notas2 = []
lst_notas3 = []
lst_notas4 = []
lst_notas5 = []
lst_medias = []

for i in range (1,6,1):
    professor = input(f"Digite o nome do professor {i}:")
    lst_professores.append(professor)
    
for x in range (1,6,1):  
    for i in range (1,9,1):
        professores = x - 1
        nota = float(input(f"O aluno {i} deve digitar uma nota para {lst_professores[professores]}: "))
        if nota not in range(1,6):
            print("")
            print("Por favor, insira um valor válido de 1 a 5.")
            exit()
        elif nota in range (1,6):
            globals()[f'lst_notas{x}'].append(nota)
            continue
        
for x in range (1,6,1):
    y = x - 1
    notasfinais = globals()[f'lst_notas{x}']
    media = sum(notasfinais)/8
    lst_medias.append(media)
    print(f"""
    {lst_professores[y]}:
    {notasfinais}
    
    Nota média:
    {media}
    """)
melhor = lst_medias.index(max(lst_medias))    
pior = lst_medias.index(min(lst_medias))  
print(f"O professor com a maior nota é {lst_professores[melhor]}, tendo {max(lst_medias)} de média e o com a menor é {lst_professores[pior]} com {min(lst_medias)} de média.")
      