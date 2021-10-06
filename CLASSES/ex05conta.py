class Conta:
    def __init__(self, nro_conta, titular, saldo = 0):

        self.nro_conta = nro_conta
        self.titular = titular
        self.saldo = saldo

    def alteraTitular(self, novoNome):
        
        self.titular = ""
        self.titular = novoNome 
        print("Nome do titular alterado com sucesso!!!")
        print("Novo nome: ", self.titular)
    
    def consultaSaldo(self):
        print("Seu saldo atual é: ", self.saldo)

    def deposito(self, vr_deposito):

        self.saldo += vr_deposito
        print("Valor depositado: ", vr_deposito)
        print("Novo saldo: ", self.saldo)

    def saque(self, vr_saque):
    
        self.saldo -= vr_saque
        print("Valor sacado: ", vr_saque)
        print("Novo saldo: ", self.saldo)    