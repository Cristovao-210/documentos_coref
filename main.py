import streamlit as st
from auxiliares.var_globais import *
from formularios.ato.formulario_atos import *

st.set_page_config(page_title="Atos UnB")
st.subheader("GERADOR DE DOCUMENTOS OFICIAIS")

dados_do_formulario = {}
dados_do_formulario['documento_selecionado'] = st.sidebar.selectbox("Tipo de Documento", lista_de_documentos)

if dados_do_formulario['documento_selecionado'] == "Ato":
    dados_do_formulario['acao_com_documento'] = st.sidebar.selectbox("Solicitação", ("", "Gerar Ato", "Preparar para Publicação"))
    if dados_do_formulario["acao_com_documento"] == 'Gerar Ato':
        dados_do_formulario['setor_responsavel'] = st.sidebar.selectbox("Setor Responsável", lista_de_setores)
        if dados_do_formulario['setor_responsavel'] != "":
            dados_do_formulario['finalidade_do_ato'] = st.sidebar.selectbox("Finalidade do ato", lista_finalidades_do_ato)
            if dados_do_formulario['finalidade_do_ato'] == "Manutenção de Funções":
                dados_do_formulario['tipo_de_ato'] = st.sidebar.selectbox("Informe o tipo de ato", lista_de_tipos_de_ato)
                if dados_do_formulario["tipo_de_ato"] != "":
                    # detalhe em nomeação de cd
                    if dados_do_formulario["tipo_de_ato"] == "Nomeação de CD":
                        dados_do_formulario["ja_possui_funcao"] = st.sidebar.radio("Já possuí Função?", ("Não", "Sim"), )
                        if dados_do_formulario['ja_possui_funcao'] == "Sim":
                            dados_do_formulario['genero'] = st.sidebar.radio("Informe o Gênero", ("Masculino", "Feminino"))
                        else:
                            dados_do_formulario['genero'] = ""
                    # detalhe em exoneração de cd - parte final do texto
                    if dados_do_formulario["tipo_de_ato"] == "Exoneração de CD":
                        dados_do_formulario['termino_de_mandato'] = st.sidebar.radio("É por término de mandato? ", ("Sim", "Não"))
                    # detalhe em substituição de cd - 
                    if dados_do_formulario["tipo_de_ato"] == "Substituição de CD" or dados_do_formulario["tipo_de_ato"] == "Substituição de FG" or dados_do_formulario["tipo_de_ato"] == "Substituição de FCC":
                        dados_do_formulario['cargo_vago'] = st.sidebar.radio("É de Cargo Vago? ", ("Sim", "Não"))
                    
                    formulario_gerar_ato(dados_do_formulario)


# verificando salvamento das informações
#st.write(dados_do_formulario)
    