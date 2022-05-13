'''
EXERCÍCIO 

Faça uma lista de tarefas com as seguintes opções :
    adicionar tarefa
    listar tarefa 
    opção de desfazer ( a cada vez que chamarmos, desfaz a última ação)
    opção de refazer  (a cada vez que chamarmos, refaz a última ação)

    ['TAREFA 1', 'TAREFA 2']
    ['TAREFA 1'] <- Desfazer
    ['TAREFA 1', 'TAREFA 2'] <-Refazer 
    
    
    
    input <- Nova tarefa
'''

def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()

def do_redo(todo_list,redo_list):
    if not redo_list:
        print('Nada a refazer')
        return
    
    last_redo = redo_list.pop()
    todo_list.append(last_redo)
    
    
def do_undo(todo_list,redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)
    

def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []
    
    while True: 
        todo = input('digite uma tarefaou undo redo, ls: ')
        
        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list,redo_list)
            continue
        
        elif todo == 'redo':
            do_redo(todo_list,redo_list)
            continue
        
        
        do_add(todo, todo_list)
            
    

