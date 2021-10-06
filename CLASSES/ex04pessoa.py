class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def Crescer(self):
        if self.idade < 21:
            self.altura += 0.5
    def Envelhecer(self):
        self.idade += 1
        self.Crescer()
        print(f"{self.nome} envelheceu um ano!!!")
    def Engordar(self, var_peso):
        self.peso += var_peso
        print(f"{self.nome} engordou!!!!\n{self.peso} é seu novo peso")

        