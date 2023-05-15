import functions
while True:
    user_option = input("Type add, show, edit, complete or exit: ")
    user_option = user_option.strip().lower()
    if 'add' in user_option:
        todos = functions.get_todos()
        todo = input("Enter a TODO: ") + "\n"
        todos.append(todo.title())
        functions.write_todos(todos)

    elif 'show' in user_option:
        todos = functions.get_todos('todos.txt')
        for index, todo in enumerate(todos):
            new_todo = todo.strip("\n")
            print(f'({index + 1}).{new_todo.title()}', )
    elif 'edit' in user_option:
        todos = functions.get_todos('todos.txt')
        index_todo_edit = int(input("Introduce el número del TODO que deseas editar: "))
        text = input("Ingresa el nuevo valor: ")+"\n"
        try:
            todos[index_todo_edit-1] = text.title()
            functions.write_todos(todos)
            print("Great the TODO has been updated")
        except Exception as e:
            print("Parece que has introducido un valor que no está en la lista de TODOS")
    elif 'complete' in user_option:
        todos = functions.get_todos('todos.txt')
        index_todo_to_complete= int(input("Number of TODO to complete: "))-1
        todo_to_complete = todos[index_todo_to_complete].strip('\n')
        try:
            todos.pop(index_todo_to_complete)
            functions.write_todos(todos)
            print(f"Todo {todo_to_complete} was completed")
        except Exception as e:
            print("Parece que has introducido un valor que no está en la lista de TODOS")

    elif 'exit' in user_option:
        break
    else:
        print("option not allow")
