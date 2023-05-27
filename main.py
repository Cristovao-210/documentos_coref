import streamlit as st
from auxiliares.var_globais import *

st.subheader("GERADOR DE DOCUMENTOS OFICIAIS")

documento_selecionado = st.sidebar.selectbox("Tipo de Documento", lista_de_documentos)
if documento_selecionado == "Ato":
    setor_responsavel = st.sidebar.selectbox("Setor Responsável", lista_de_setores)
    