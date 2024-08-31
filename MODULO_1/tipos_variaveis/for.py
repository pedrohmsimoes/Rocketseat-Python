print("For utilizando lista")
lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)

print("For utilizando tupla")
tupla = (1,2,3,4,5)
for elemento in tupla:
    print(elemento)

pessoa = {"name": "Pedro", "Idade": "21", "cidade": "Sao Paulo"}
print("For utilizando dicionario - chaves")
for chave in pessoa.keys():
    print(chave)

print("For utilizando dicionario - values")
for valor in pessoa.values():
    print(valor)

print("For utilizando dicionario - items")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# renge(): intervalo numerico
#[0,1,2,3,4,5,6,7,8,9]

print(list(range(0,10)))
print("\n utilizando a funçao range()")
for numero in range(5):
    print("numero:", numero)

print("\n utilizando a funçao range() com len")
for indice in range(0,len(lista)):
#    print("indice:", indice)
#    print("elemento:", lista[indice])
    if indice == 3:
        lista[indice]= 5
    else: 
        lista[indice] = 0
    print(lista)

# enumerate()

listaEnumerate = ["a", "b", "c"]
for indice, valor in enumerate(listaEnumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("indice 1")
