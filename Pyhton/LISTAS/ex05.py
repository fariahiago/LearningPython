a = []
pares = []
impares = []

for i in range(20):
    a.append(int(input("Digite o nomero: ")))
    if a[i] % 2 == 0:
        pares.append(a[i])
    else:
        impares.append(a[i])
print("Numeros digitados: ", a)
print("Pares: ", pares)
print("Impares: ", impares)