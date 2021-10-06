def valorPgto(vr_prest, dias_atraso):
    if dias_atraso == 0:
        return vr_prest
    else: 
        vr_fin = vr_prest * 1.03 + ((0.01 * vr_prest) * dias_atraso)
        return vr_fin

balancoDia = []
idPgto = 0
somaDia = 0


print("<<<<<<<<<<<<<LANÇAMENTO DE PAGAMENTOS RECEBIDOS: >>>>>>>>>>>>>>")

while True: 
    registro_pgto = []
    vr_parcela = float(input("Digite o valor da prestação a ser paga: "))
    if vr_parcela == 0:
        break
    else: 
        qt_dias_atraso = int(input("Digite a quantidade de dias em atraso: "))

        vr_final = valorPgto(vr_parcela, qt_dias_atraso)

        check_pay = input(f"O valor final a ser pago é de: {vr_final}\n"
                          "Deseja confirmar o pagamento? \n"
                          "<S> para Sim /// <N> para Não")
        if check_pay == 'S':
            
            idPgto += 1
            registro_pgto.append(idPgto)
            registro_pgto.append(vr_final)
            somaDia += vr_final
        balancoDia.append(registro_pgto)
        registro_pgto.clear
    
print("<<<<<<RELATORIO DO DIA >>>>>>> ")
print("Valor Total recebido: ", somaDia)
print(balancoDia)

        
