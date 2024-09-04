def adicionar_tarefa(tarefa, lista):
    return lista.append(tarefa)

tarefas=[]
memoria_tarefas = []
while True:
    comando = input("Digite uma tarefa ou um comando: ")
    if comando == 'listar':
        for tarefa in tarefas:
            print(tarefa)
    elif comando == 'desfazer':
        if tarefas == []:
            print('Não há nada para refazer.\n')
        else:
            memoria_tarefas.append(tarefas[-1])  
            tarefas.pop()

    elif comando == 'refazer':
        if memoria_tarefas == []:
            print('Não há nada para refazer.')
        else:
            tarefas.append(memoria_tarefas[-1])
            memoria_tarefas.pop()
    else:
        adicionar_tarefa(comando,tarefas)
    
    