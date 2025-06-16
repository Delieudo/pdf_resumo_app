import streamlit as st
import fitz  # PyMuPDF

st.set_page_config(page_title="Resumo de PDF com IA", page_icon="📄")

st.title(" Resumidor de PDF com Ia")
st.write("Faça upload de um PDF e resuma com inteligência artificial.")

uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

if uploaded_file:
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = "\n".join([page.get_text() for page in doc])

    st.session_state["conteudo_pdf"] = text
    st.success("PDF carregado com sucesso!")

    if st.button("Ir para próxima tela"):
        st.switch_page("pages/1_Conteudo_extraido.py")
