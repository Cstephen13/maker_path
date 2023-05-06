def get_todos(file_path="todos.txt"):
    """
    Read a text file and return the list of to-do items
    :param file_path:
    :return: list todos
    """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_to_write, file_path="todos.txt"):
    """
    Write to-do items list in the text file
    :param todos_to_write:
    :param file_path:
    :return: None
    """
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_to_write)