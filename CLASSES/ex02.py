class Quadrado():
    self.lado = lado
    
    def valorLado(self): 
        Quadrado.lado = int(input("Digite o valor do lado do quadrado: "))
    
    def retornaValorLado(self): 
        print(Quadrado.lado)
    
    def calculaArea(self):
        return Quadrado.lado * Quadrado.lado
