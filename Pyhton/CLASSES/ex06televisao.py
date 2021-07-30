class TV:
    def __init__(self,smartv, num_canal = 4, volume = 15):
        
        self.smartv = input(bool("É SmarTV? (True/False)"))
        self.num_canal = num_canal
        self.volume = volume
    def mudaCanal(self, novo_canal):
        if novo_canal > 0 and novo_canal < 100:
            self.num_canal = novo_canal
            print("Voce mudou para o canal ", novo_canal)
        else: 
            print("Canal Invalido, refaça a operação")
    def alteraVolume(self, var_volume):
        if (var_volume + self.volume) > 100 or  (var_volume + self.volume) < 0:
            self.volume += var_volume
            print("Novo Volume: ", self.volume)
        else:
            print("Volume invalido, repita a operação")