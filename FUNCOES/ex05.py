def somaImposto(custo_inicial, tx_imposto):
    var = (tx_imposto/100) + 1
    custo_final = var * custo_inicial
    return(custo_final)

precoDeCusto = float(input("Digite o preço de custo do produto: "))
v_Imposto = int(input("Digite a taxa aplicada ao produto acima: (em %)"))

custo_final = somaImposto(precoDeCusto,v_Imposto)

print("O custo final do produto acima é: %.2f" % custo_final)