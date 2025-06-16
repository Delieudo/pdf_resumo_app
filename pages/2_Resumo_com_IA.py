import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="Resumo gerado", page_icon="")

st.title(" Resumo com IA")

# Pegue o conteúdo do PDF
if "conteudo_pdf" not in st.session_state:
    st.error("Por favor, volte e envie um PDF primeiro.")
    st.stop()

# Configure sua chave da OpenAI
openai_api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("API Key da OpenAI não encontrada. Configure em st.secrets ou variável de ambiente.")
    st.stop()

client = OpenAI(api_key=openai_api_key)

if st.button("Gerar resumo"):
    with st.spinner("Gerando resumo..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",  # ou "gpt-3.5-turbo"
                messages=[
                    {"role": "user", "content": f"Resuma o seguinte texto:\n\n{st.session_state['conteudo_pdf'][:12000]}"}
                ],
                max_tokens=500,
                temperature=0.5,
            )
            resumo = response.choices[0].message.content
            st.subheader("Resumo:")
            st.write(resumo)
        except Exception as e:
            st.error(f"Erro ao chamar a API: {e}")
