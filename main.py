import streamlit as st
from auxiliares.var_globais import *

st.subheader("GERADOR DE DOCUMENTOS OFICIAIS")

documento_selecionado = st.sidebar.selectbox("Tipo de Documento", lista_de_documentos)
if documento_selecionado == "Ato":
    acao_com_documento = st.sidebar.selectbox("Setor Responsável", ("", "Gerar Ato", "Preparar para Publicação"))
    # teste commit
    