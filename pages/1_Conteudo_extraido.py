import streamlit as st

st.set_page_config(page_title="Conteúdo extraído", page_icon="📝")

st.title(" Conteúdo do PDF")

if "conteudo_pdf" not in st.session_state:
    st.error("Por favor, volte e envie um PDF primeiro.")
    st.stop()

texto = st.session_state["conteudo_pdf"]

st.text_area("Texto extraído:", value=texto[:3000], height=300)

if st.button("Resumir com IA"):
    st.switch_page("pages/2_Resumo_com_IA.py")
