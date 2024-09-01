# criando uma tupla de exemplo

minha_tupla = (1, 2, 2, 3, 4)
print("minha tupla", minha_tupla)

print("minha tupla[0]", minha_tupla[0])
print("minha tupla[2]", minha_tupla[2])
print("minha tupla[-1]", minha_tupla[-1])

# tupulas nao podem ser mudadas 

#metodo count

contagem = minha_tupla.count(2)
print("quantidade de elemento aparece [2]:", contagem)

# metodo index

indece = minha_tupla.index(3)
print("indece da primeira ocorrencia do elemento 3:", indece)