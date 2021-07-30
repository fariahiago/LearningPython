ordem = ('Primeiro', 'Segundo', 'Terceiro', 
         'Quarto', 'Quinto','Sexto','Setimo',
         'Oitavo','Nono','Decimo')
caract = []
consoantes = []
numConsoantes = 0

for i in ordem: 
    caract.append(input("%s caracter: " %i))

a = len(caract)
caract.remove('a')
caract.remove('e')
caract.remove('i')
caract.remove('o')
caract.remove('u')

numConsoantes = a - len(caract)
print("Foram inseridas ", numConsoantes, " consoantes, que foram: ", caract)