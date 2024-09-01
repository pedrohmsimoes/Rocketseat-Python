# declaraçao
nome_completo = "Pedro Simoes"

nomeCompletoApstas = """Pedro
simoes"""

nome_completo_quebra = "pedro \
simoes "

nome = "pedro"
sobrenome= "simoes"


# Formataçao

print("Nome Completo (1a forma):", nome_completo)
print("Nome Completo (2a forma):" + nome_completo)
print("Nome Completo (3a forma):" + "Pedro" + "Simoes")
print("Nome Completo (4a forma):" + "Pedro", "Simoes")
print("Nome Completo (5a forma):", nomeCompletoApstas )
print("Nome Completo (6a forma):", nome_completo_quebra)
print("Nome Completo (7a forma): %s" % nome_completo )
print("Nome Completo (8a forma): %s %s" % (nome, sobrenome) )
print(f"Nome Completo (9a forma): {nome} {sobrenome}" )
print("Nome Completo (10a forma): {} {}".format(nome, sobrenome) )