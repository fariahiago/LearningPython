ordem = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto',
         'Quinto', 'Sexto', 'Setimo', 'Oitavo', 'Nono', 'Decimo')
num = []
quad = []
for i in ordem:
    num.append(int(input("%s numero: " %i)))
print(num)
for i in range(10):
    num[i] = num[i] * num[i]

print(num)
print(sum(num))