print("\nexemplo de captura de exceçoes")
try: 
    numero = input("digite um numero inteiro:")
    resultado = 10 / int(numero)
except ValueError as e:
    print(f"Erro de value erro: {e}")
except Exception as e:
    print(f"Eroo: {e}")
else:
    print(f"resultado: {resultado}")
finally:
    print("Operaçao finalizada")