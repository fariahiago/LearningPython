def converteHora(a_ou_p, hora, min):
    if a_ou_p == 'P':
        hora += 12
    return f"São {hora}:{min}."
        
        




print("=================CONVERSOR DE HORARIO================\n")

while True:
    a = input("CONVERTENDO HORARIO\n\nOpções:\n"
              "1- Digite 'A' para um horário A.M.\n"
              "2 - Digite 'P' para um horário P.M.\n"
              "3- Digite 'F' para encerrar o programa\n")
    
    if a == 'F':
        print("Fim do programa")
        break
    else: 
        hor = int(input("Digite as horas: "))
        min = int(input("Digite os minutos: "))

        resp = converteHora(a,hor,min)
        print(resp)