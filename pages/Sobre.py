import streamlit as st

st.write(
    "Olá, use este app como seu bloco de notas online ou uma simples lista de afazeres futuros. \n"
    "Como usar: o app já vem com 4 anotações aleatórias, mas voce pode incluir outros itens ou \n"
    "excluí-los clicando em cada um. Para inserir uma nova tarefa, escreva no campo de texto e pressione \n"
    "ENTER para adicionar o item na lista. A tarefa é inserida na tela logo abaixo da entrada."
)

# 02 quebras de linha “em branco” entre os blocos
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    "Desenvolvido por: Danilo dos Santos Soares <br>"
    "Interface: Streamlit <br>"
    "© 2025 - Todos os direitos reservados.",
    unsafe_allow_html=True
)
