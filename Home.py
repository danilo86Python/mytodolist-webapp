import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:
        todos.append(todo)
        functions.write_todos(todos)

st.title("Meu aplicativo de tarefas")
# st.subheader("Esta é uma interface Streamlit.")
st.write("Registre coisas importantes e não perca a <b>produtividade:</b>",
         unsafe_allow_html=True)

st.text_input(label="New item", placeholder="Adicione seus compromissos aqui...",
              on_change=add_todo, key="new_todo", label_visibility="collapsed")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}_{todo}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{index}_{todo}"]
        st.rerun()