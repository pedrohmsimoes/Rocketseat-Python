# Exemplo
def saudacao(nome):
    print(f"Ola, {nome}!")

print("\nChamando a funçao saudacao:")
saudacao("Alice")
saudacao("Pedro")

# funçao com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando a funçao quadrado:")
resultado_quadrado = quadrado(6)
print("resultado da funçao do quadrado", resultado_quadrado)

# funçao com multiplos parametros
def soma(numero1, numero2):
    resultado = (numero1 + numero2)
    return resultado

print("\nChamando a funçao soma:")
numero1 = 20
numero2 = 54

resultado_soma = soma(numero1, numero2)
print("a sina do numero %s e numero %s e: %s" % (numero1, numero2, resultado_soma))