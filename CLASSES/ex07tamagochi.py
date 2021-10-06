class Tamagushi:
    def __init__(self, nome, fome = 0, saude = 10, idade = 0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        print("Construtor Finalizado!")
    
    def changeName(self, nome):
        self.nome = nome
        print("Nome alterado com sucesso!\nNovo nome:", self.nome)
    
    def Alimentar(self):
        if self.fome == 10:
            print(self.nome, " está cheio!!!")
        else:
            self.fome += 1
            print(self.nome, " comeu!")
    
    def idade(self):
        self.idade += 1
    
    def retornaNome(self):
        print(self.nome)
    

