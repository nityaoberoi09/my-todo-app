FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ read a text file and return
     the list of todo items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


# print(help(get_todos))
def write_todos(todos_arg, filepath=FILEPATH):
    """ write a todos item list in text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    # closing the file so that it doesnt make any change in content of file


if __name__ == "__main__":
    print("hello")
    print(get_todos())
#== here is not assignment ooerator
#this will be executed only when this script
# is executed directly as the main script then
# we want to execute the function otherwise if this
# is imported from another file then this wont work