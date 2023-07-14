import streamlit as st
from auxiliares.var_globais import *
from auxiliares.connection import *
from auxiliares.funcoes import *
from formularios.ato.formulario_atos import *
from documentos.ato.partes_do_ato import preambulo_ato



st.set_page_config(page_title="Atos UnB")

# COLOCAR CRIAÇÃO DO BANDO DE DADOS AQUI
conex = criar_conexao('atosgerados_db')
criar_tabela(conex)

st.markdown("<h4 style='text-align: center; background: #B52E3A; color: white;'>GERADOR DE DOCUMENTOS OFICIAIS</h4>", unsafe_allow_html=True)

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
                        dados_do_formulario["ja_possui_funcao"] = st.sidebar.radio("Já possuí Função?", ("Não", "Sim"))
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
                    # detalhe não remunerada
                    if dados_do_formulario["tipo_de_ato"] == "FCC não remunerada":
                        dados_do_formulario['tipo_nao_remunerada'] = st.sidebar.radio("Tipo", ("Designação", "Dispensa"))
                    formulario_gerar_ato(dados_do_formulario)

    elif dados_do_formulario['acao_com_documento'] == "Preparar para Publicação":
        
        st.markdown("<br><h6 style='text-align: center;'>Gerar documento para publicação</h6>", unsafe_allow_html=True)

        # criando bando de dados, tabela, inserção e busca
        data_publicacao = st.date_input('Informe a data de emissão do ato: ')
        conectar = criar_conexao('atosgerados_db')
        if data_publicacao != "":
            data_publicacao = data_convertida_br(str(data_publicacao))
            dicionario_publicacao = selecionar_atos(conectar,'atos_publicacao', data_publicacao)
            if dicionario_publicacao.empty:
                st.info("Nenhum Ato foi registrado na data selecionada.")
            else:
                st.write(dicionario_publicacao.sort_values(by='NUMERO'))
                #marcador = st.data_editor(dicionario_publicacao, num_rows= "dynamic")
                col_btn_1, col_btn_2, col_btn_3= st.columns([3,3,2])
                with col_btn_1:
                    pass
                with col_btn_2:
                    btn_gerar_word = st.button("Gerar Documento>>")
                with col_btn_3:
                    pass
                if btn_gerar_word:
                    word_dict = dict(dicionario_publicacao.sort_values(by='NUMERO'))
                    gerar_word_publicacao(word_dict)
                
                    
                
            
            
            
        