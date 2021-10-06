def p_ou_n(num1):
    if num1 >= 0:
        return 'Positivo'
    else: 
        return 'Negativo'

while True: 
    a = int(input("Digite um numero para saber se ele é positivo ou negativo:\nDigite '666' para encerrar:\n"))
    if a == 666:
        break
    else: 
        b = p_ou_n(a)
        print(b)

print("Fim do programa")