import streamlit as st
from auxiliares.var_globais import *
from documentos.ato.base_do_ato import gerar_ato



def formulario_gerar_ato(dados_do_formulario):

    #st.subheader(f"FORMULÁRIO PARA COMPOSIÇÃO DE DOCUMENTOS: {dados_do_formulario['documento_selecionado']}")
    setor_responsavel = dados_do_formulario['setor_responsavel']

    with st.form('form_ato', clear_on_submit=True):

        dados_do_formulario['numero_ato'] = st.text_input('Informe o número do Ato')
        dados_do_formulario['numero_do_sei'] = st.text_input('Informe o número do Processo SEI')

        # 0-categoria_cargo (o(a) Docente/Servidor(a)/o Professor do Magistério Superior/a Professora do Magistério Superior) 
        dados_do_formulario['categoria_funcional'] = st.selectbox("Catergoria Funcional", lista_de_categorias_funcionais)
        # 1-nome
        dados_do_formulario['nome_servidor'] = st.text_input('Nome do Servidor')
        # 2-nome_COORDENAÇÃO/DIREÇÃO, (Coordenador(a) de Pós-graduação/Coordenador(a) de Graduação), 3-descrição do curso a ser coordenado
        dados_do_formulario['nome_da_funcao'] = st.selectbox("Nome da Função", lista_de_nome_funcoes)
        # 3- cd-1 a 4,fg-1 a 3,fcc
        dados_do_formulario['tipo_de_funcao']  = st.selectbox("Tipo de Função", lista_de_tipos_funcoes)
        # quando substituição #['a Coordenadora', 'o Coordenador', 'o Diretor', 'a Diretora', 'outros']
        dados_do_formulario['cargo_a_ser_substituido'] = st.selectbox("Cargo a ser substituído", ("","em construção...")) # Concatenar com o nome da função]
        # assinatura
        if setor_responsavel == "DGP":
            dados_do_formulario['dirigente_responsavel'] = st.radio("Assinatura:",("Decano(a) titular", "Decano(a) em exercício"))
        elif setor_responsavel == "DGP/DAP":
            dados_do_formulario['dirigente_responsavel'] = st.radio("Assinatura:",("Diretor(a) titular", "Diretor(a) em exercício"))
        elif setor_responsavel == "REITORIA":
            dados_do_formulario['dirigente_responsavel'] = st.radio("Assinatura:",("Reitor(a)", "Vice-Reitor(a)"))

        dados_do_formulario['motivo_do_afastamento'] = ""
        dados_do_formulario['servidor_a_ser_substituido'] = ""
        dados_do_formulario['data_inicial_substuicao'] = "01/06/2023"
        dados_do_formulario['data_final_substuicao'] = "14/06/2023"
        dados_do_formulario['data_reconducao'] = "31/07/2023"
        dados_do_formulario['genero'] = "Masculino"






        btn_gera_ato = st.form_submit_button('Gerar Ato')

    if btn_gera_ato:
        gerar_ato(dados_do_formulario)

