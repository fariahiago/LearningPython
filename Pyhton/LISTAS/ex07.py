ordem = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto')
num = []
soma = 0
media = 0

for i in ordem: 
    num.append(int(input("%s numero: " %i)))
soma = sum(num)
media = sum(num)/len(num)

print(num)
print(f"Soma: {soma}\nMedia: {media}")