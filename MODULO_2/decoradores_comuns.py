# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10

    def __init__(self, nome) -> None:
        self.nome = nome # atributo da instancia

    def metodo_instancia(self):
        return f"metodo de instancia chamando para {self.nome} "

    @classmethod
    def metodo_classe(cls):
        return f"metodo de classe chamando para  o valor = {cls.valor}"

    @staticmethod
    def metodo_estatico():
        return "metodo estatico chamado"

obj = MinhaClasse(nome="classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe()) 
print(MinhaClasse.metodo_estatico())

class carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
configuracao1 = "Toyata,Corolla,2022"

carro1 = carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class matematica:
    @staticmethod
    def somar(a, b):
        return a + b
print(matematica.somar(a=10, b =23))