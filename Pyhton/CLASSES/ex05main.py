from ex05conta import Conta as ct

hiago = ct("5854771", "Hiago Oliveira de Faria")

hiago.consultaSaldo()

hiago.alteraTitular("Hiago O. Faria")

hiago.deposito(350)

hiago.saque(100)

hiago.consultaSaldo()