ordem = ('Primeira', 'Segunda', 'Terceira', 'Quarta')
alunos = []
media = 0
aprovados = 0

a = int(input("Digite a quantidade de alunos que deseja inserir: "))

for j in range(a):
    
    aluno = []
    aluno.append(input("Digite o nome: "))
    
    for i in range(4): 
        notas = []
        notas.append(float(input("Nota: ")))
    
    aluno.append(notas)

    media = sum(notas) / len(notas)
    
    if media >= 7.0:
        aprovados += 1

    aluno.append(media)
    
    alunos.append(aluno)


print(alunos)
print("Numero de aprovados:", aprovados)
    
