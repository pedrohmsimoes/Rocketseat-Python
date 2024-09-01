print("Exemplo de importação de um modulo Padrão:")
#import math
from math import sqrt
from meu_modulo import saudacao, dobro

# raiz_quadrada = math.sqrt(25) 
raiz_quadrada = sqrt(25)
print(f"Raiz quadrada de 25: {raiz_quadrada}")

print("\nExemplo de criaçao e utilizaçao de um modulo personalizado")

mensagem = saudacao("Pedro")
resultado = dobro(5)
print(mensagem)
print(f"o dobro de 5: {resultado}")