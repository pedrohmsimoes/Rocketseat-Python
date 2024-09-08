def meu_decorador(func):
    def wrapper():
        print("Antes da funçao ser chamanda")
        func()
        print("depois da funçao ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha funçao foi chamada")

minha_funcao()

class meuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> any:
        print("Antes da funçao ser chamada (decorador de classe)")
        self.func()
        print("Depois da minha funçao ser chamada (decorador de classe)")

@meuDecoradorDeClasse
def segunda_funcao():
    print("segunda funçao ser chamada")

segunda_funcao()