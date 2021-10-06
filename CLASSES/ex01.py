class Bola():
    cor = "branca"
    circunferencia = 10
    material = "Borracha"
    
    def trocaCor(self):
        Bola.cor = input("Digite a cor da bola: ")
    
    def mostraCor(self):
        print(Bola.cor) 
        

muxeba = Bola()

muxeba.trocaCor()

muxeba.mostraCor()
