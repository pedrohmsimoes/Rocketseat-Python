def adicionar_tarefa(Tarefas, nome_tarefa):
    # tarefa: nome da tarefa
    # completada: indica se essa tarefa já foi completada ou não
    Tarefa = {"nome": nome_tarefa, "completada": False}
    Tarefas.append(Tarefa)
    print(f"A tarefa '{nome_tarefa}' foi adicionada com sucesso!")
    return

def ver_tarefas(Tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(Tarefas):
        status = "✓" if tarefa["completada"] else ""
        nome_tarefa = tarefa["nome"]
        print(f"{indice + 1}. [{status}] {nome_tarefa}")

def atualizar_tarefa(Tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(Tarefas):
        Tarefas[indice_tarefa_ajustado]["nome"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para '{novo_nome_tarefa}'")
    else:
        print("indice de tarefa invalido")
    return

def tarefa_completada(Tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    Tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice_tarefa} marcado como completada")
    return

def deletar_tarefas_completadas(Tarefas):
    for tarefa in Tarefas:
        if tarefa["completada"]:
            Tarefas.remove(tarefa)
    print("Taferas completadas foram deletadas.")
    return

Tarefas = []

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(Tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(Tarefas)
    elif escolha == "3":
        ver_tarefas(Tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(Tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
        ver_tarefas(Tarefas)
        indice_tarefa = input("Digite o numero da tarefa que deseja completar:")
        tarefa_completada(Tarefas, indice_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(Tarefas)
        ver_tarefas(Tarefas)

    elif escolha == "6":
        break

print("Programa finalizado")
