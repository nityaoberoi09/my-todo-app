import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my Todo')
st.write('This App Increases ur Productivity')

count = 0
for index, todo in enumerate(todos):
    count += 1
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='.', placeholder="add a new todo.....",
              on_change=add_todo, key='new_todo')
print('hello')
st.session_state
