import functions
import PySimpleGUI as sg

todos = functions.get_todos()
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a TODO", key='todo_input')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todos, key='todos_list', enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
window = sg.Window(
    'My TO-DO App',
    layout=[[label], [input_box, add_button], [list_box, edit_button]],
    font=('Helvetica', 20)
)
while True:
    event, values = window.read()
    if event == 'Add':
        todos_copy = todos[:]
        if values.get('todo_input'):
            new_todo = values.get('todo_input') + '\n'
            todos_copy.append(new_todo)
            functions.write_todos(todos_copy)
    elif event == 'Edit':
        todos_copy = todos[:]
        todo_to_edit = values['todos_list'][0]
        new_todo = values['todo_input']
        index = todos_copy.index(todo_to_edit)
        todos_copy[index] = new_todo + '\n'
        functions.write_todos(todos_copy)
        window['todos_list'].update(todos_copy)
    elif event == 'todos_list':
        window['todo_input'].update(values[event][0].strip('\n'))
    elif event == sg.WIN_CLOSED:
        break

window.close()

