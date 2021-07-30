pessoas = []
n = int(input("Digite a quantidade de pessoas que serão adicionadas: "))

for i in range(n):
    pessoa = []
    pessoa.append(input("Digite o nome:"))
    pessoa.append(int(input("Digite a idade:")))
    pessoa.append(float(input("Digite a altura: ")))
    pessoas.append(pessoa)

print(pessoas)