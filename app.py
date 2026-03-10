import streamlit as st

st.title("Controle de Estoque")

produto = st.text_input("Nome do Produto")
quantidade = st.number_input("Quantidade", min_value=0)

if st.button("Salvar"):
    st.success("Produto salvo!")
    st.write("Produto:", produto)
    st.write("Quantidade:", quantidade)
