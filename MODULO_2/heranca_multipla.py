class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

class mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} esta amamentando"

class ave(Animal):
    def voar(self):
        return f"{self.nome} esta voando"

class morcego(mamifero, ave):
    def emitir_som(self):
        return "morcegos emitem sons ultrassonicos"

morcego = morcego(nome="batman")

# Acessando metodos da classe base Aminal
print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())
# Acessando metodos das classes Mamifer e ave
print("morcengo amamentando:", morcego.amamentar())
print("morcego voando:", morcego.voar())