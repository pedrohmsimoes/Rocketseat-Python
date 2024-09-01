# Criando um dicionario de exemplo

pessoa = {"nome": "Pedro", "idade": 30, "cidade": "Sao Paulo"}
print("Meu dicionario de exemplo", pessoa)

# Acessando valores por chaves

print("nome:", pessoa["nome"])
print("idade:", pessoa["idade"])
print("cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Simoes"
print("sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 32
print("idade atualizada", pessoa["idade"])

# removendo um par chave vaor
del pessoa["sobrenome"]
print("removendo do dicionario", pessoa)

# metodos: keys(), values(), items()


chaves = list(pessoa.keys())
print("chaves do dicionario", chaves)
print("primeira chave", chaves[0])

valores = list(pessoa.values())
print("valores do dicionario:", valores)
print("primeiro valor do dicionario", valores[0])

itens = list(pessoa.items())
print("pares chaves valor do dicionario:", itens)
print("primeiro valor:", itens[0][1])
print("primeiro chave-valor: %s = %s " % (itens[0][0], itens[0][1]))