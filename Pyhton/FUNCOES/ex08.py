def qtosDigitos(num):
    a = num
    dig = 0
    cont = 10
    while a > 0:
        a = a - cont
        dig += 1
        cont *= 10
    return dig    

while True:
    a = int(input("Digite o numero a ser verificado: "))
    if a == 0:
        break
    else:
        b = qtosDigitos(a)
        print(f"O numero {a} tem {b} digito(s)")