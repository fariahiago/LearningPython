class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def define_Base_e_Alt(self, base, altura): 
        self.base = base
        self.altura = altura

    def retorna_Lados(self):
        print(f"Os lados do retângulo são: {self.base} e {self.altura}")

    def calculaPerimetro(self): 
        self.perimetro = (self.base * 2) + (self.altura * 2)
        print(self.perimetro)

    def calculaArea(self): 
        self.area = self.base * self.altura
        print(self.area)