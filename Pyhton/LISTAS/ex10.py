ordem = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto',
         'Quinto', 'Sexto', 'Setimo', 'Oitavo', 'Nono', 'Decimo')
lista1 = []
lista2 = []
listafinal = []
for i in ordem:
    lista1.append(int(input("%s numero da lista 1: " %i)))

for i in ordem:
    lista2.append(int(input("%s numero da lista 2: " %i)))

for i in range(10):
    listafinal.append(lista1[i])
    listafinal.append(lista2[i])

print(lista1)
print(lista2)
print(listafinal)