textoSaltos = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto')
nomeAtleta = ' '
atletas = {}

while (nomeAtleta != ''):
    nomeAtleta = input("Atleta:")
    if(nomeAtleta != ''):
        saltos = []
        for i in textoSaltos:
            saltos.append(float(input('%s Salto: ' % i)))
        atletas[nomeAtleta] = saltos

print("\nResultado Final:")

somaSaltos = 0
media = 0

for (nomeAtleta, saltos) in atletas.items():
    print ("Atleta: %s" % nomeAtleta)
    print ("Saltos: ", saltos)
    somaSaltos = sum(saltos)
    media = somaSaltos / len(saltos)
    print ("Media dos Saltos: ", media, " m")
