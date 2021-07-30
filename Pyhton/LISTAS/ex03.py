ordem = ('Primeira', 'Segunda', 'Terceira', 'Quarta')
notas = []
media = 0
for i in ordem: 
    notas.append(float(input("%s nota: " %i)))

media = sum(notas) / len(notas)
print(notas,"Media: ", media)