
# classe exemplo
class Pessoa: 
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Ola, meu nome é {self.nome} e eu tenho {self.idade} anos."

#Objetos
pessoa1 = Pessoa("Pedro", 21)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("joao", 24)
mensagem = pessoa2.saudacao()
print(mensagem)