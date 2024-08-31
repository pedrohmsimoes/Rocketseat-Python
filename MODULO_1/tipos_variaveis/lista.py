# Declaraçao

minha_lista = [1, 2, 3, 4, 5, "Pedro", True, False]
listaNumerica = [341, 22, 3, 4, 35]

# Exibindo a lista
print("minha lista de exemplo", minha_lista)

# Exibindo a lista em indece

minha_lista[0]= "python"

print("minha lista de exemplo com alteraçao", minha_lista)

print("indece 0", minha_lista[0])
print("indece 5", minha_lista[5])
print("lista do 1 ao 7 ", minha_lista[1:7])
print("lista do 0 ao 5", minha_lista[:6])
print("lista do indece 2 ao 7", minha_lista[2:])

# Metodos de lista

#metodo appemnd(): adiciona um elemento ao final da lista

minha_lista.append(6)
print("apos append(6):", minha_lista)

# metodo index
indice = minha_lista.index(6)
print("indece do elemento (6): ", indice)

# metedo insert: insere um lemento em um indece especifico 

minha_lista.insert(2, 10)
print("apos o insert ", minha_lista)

# metodo pop: remove e retorna o elemento

elemento_removido = minha_lista.pop(3)
print("elemento removido:", elemento_removido)
print("apos o pop(3):", minha_lista)

#metodo remove

minha_lista.remove(True)
print("apos o remove:", minha_lista)

#metodo sort
listaNumerica.sort()
print("apos sort()", listaNumerica)
