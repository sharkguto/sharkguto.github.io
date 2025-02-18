import streamlit as st

st.title("Meu Primeiro App com stlite")
st.write("Este é um exemplo de como usar o Streamlit no navegador.")

# Adicionando um botão para interatividade
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")
