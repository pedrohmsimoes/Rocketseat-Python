# exemplo de herança
print("\nExemplo de herança")
class Animal:
    def __init__(self, nome)-> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass 

class cachorro(Animal):
    def emitir_som(self):
        return "au, au"

class gato(Animal):
    def emitir_som(self):
        return "miau!"

dog = cachorro("Thor")
cat = gato("fenix")

print("\nExemplo de polimorismo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de encapsulamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self. __saldo = saldo # Atributo privado
        
    def depositar (self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(saldo = 1000)
print(f"saldo da conta bancaria: {conta.consultar_saldo()}")
conta.depositar(valor = 500)
print(f"saldo da conta bancaria: {conta.consultar_saldo()}")
conta.sacar(valor = 230)
print(f"saldo da conta bancaria: {conta.consultar_saldo()}")

print("\n exemplo de abstraçao")

from abc import ABC, abstractmethod

class veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"

    def desligar(self):
        return "carro desligado usando a chave"

carro_branco = Carro()
print(carro_branco.ligar())
print(carro_branco.desligar())