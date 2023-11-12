import random
aluno1=(input('Digite o nome do primeiro aluno:\t'))
aluno2=(input('Digite o nome do segundo aluno:\t'))
aluno3=(input('Digite o nome do terceiro aluno:\t'))
aluno4=(input('Digite o nome do quarto aluno:\t'))
lista=(aluno1,aluno2,aluno3,aluno4)
sorteio=random.sample(lista,4)
print(sorteio)

