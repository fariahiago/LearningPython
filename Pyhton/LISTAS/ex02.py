ordem = ('Primeiro', 'Segundo', 'Terceiro', 
         'Quarto', 'Quinto','Sexto','Setimo',
         'Oitavo','Nono','Decimo')
num = []
for i in ordem: 
    num.append(int(input("%s numero: " %i)))

num.reverse()
print(num)