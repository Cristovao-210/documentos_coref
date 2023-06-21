import streamlit as st
from auxiliares.var_globais import *
from documentos.ato.base_do_ato import gerar_ato



def formulario_gerar_ato(dados_do_formulario):

    #st.subheader(f"FORMULÁRIO PARA COMPOSIÇÃO DE DOCUMENTOS: {dados_do_formulario['documento_selecionado']}")
    setor_responsavel = dados_do_formulario['setor_responsavel']
    tp_ato = dados_do_formulario["tipo_de_ato"]

    with st.form('form_ato', clear_on_submit=True):

        coluna_1, coluna_2 = st.columns(2)
        with coluna_1:
            dados_do_formulario['numero_ato'] = st.text_input('Informe o número do Ato')
            dados_do_formulario['numero_do_sei'] = st.text_input('Informe o número do Processo SEI')
            # 1-nome
            dados_do_formulario['nome_servidor'] = st.text_input('Nome do Servidor')
            dados_do_formulario['descricao_da_funcao'] = st.text_input("Descrição da função", placeholder="Ex: da Faculdade de Tecnologia")
            
            
        with coluna_2:
            dados_do_formulario['ano_do_ato'] = st.text_input('Ano do Ato', value=ano_atual)
            # 0-categoria_cargo (o(a) Docente/Servidor(a)/o Professor do Magistério Superior/a Professora do Magistério Superior) 
            dados_do_formulario['categoria_funcional'] = st.selectbox("Catergoria Funcional", lista_de_categorias_funcionais)
            # 2-nome_COORDENAÇÃO/DIREÇÃO, (Coordenador(a) de Pós-graduação/Coordenador(a) de Graduação), 3-descrição do curso a ser coordenado
            dados_do_formulario['nome_da_funcao'] = st.selectbox("Nome da Função", lista_de_nome_funcoes)
            # 3- cd-1 a 4,fg-1 a 3,fcc
            dados_do_formulario['tipo_de_funcao']  = st.selectbox("Tipo de Função", lista_de_tipos_funcoes)
            
           
            
            
            
            
           
            
        if tp_ato == "Substitução de CD" or tp_ato == "Substitução de FG" or tp_ato == "Substitução de FCC":    
            # quando substituição #['a Coordenadora', 'o Coordenador', 'o Diretor', 'a Diretora', 'outros']
            dados_do_formulario['cargo_a_ser_substituido'] = st.selectbox("Cargo a ser substituído", lista_de_nome_funcoes) # Concatenar com o nome da função]
            dados_do_formulario['motivo_do_afastamento'] = st.text_input("Durante o período de: ", placeholder="Ex.: Férias, Licença Capacitação, etc")
            dados_do_formulario['servidor_a_ser_substituido'] = st.text_input("Nome do Titular a ser substituído: ")
            dados_do_formulario['data_inicial_substuicao'] = st.date_input("Início da Substituição: ")
            dados_do_formulario['data_final_substuicao'] = st.date_input("Término da Substituição: ")
            dados_do_formulario['genero'] = "Masculino"
        elif tp_ato == "Recondução de CD":        
            # Recondução
            dados_do_formulario['data_reconducao'] = "31/07/2023"




        # assinatura
        if setor_responsavel == "DGP":
            dados_do_formulario['dirigente_responsavel'] = st.radio("Assinatura:",("Decano(a) titular", "Decano(a) em exercício"))
        elif setor_responsavel == "DGP/DAP":
            dados_do_formulario['dirigente_responsavel'] = st.radio("Assinatura:",("Diretor(a) titular", "Diretor(a) em exercício"))
        elif setor_responsavel == "REITORIA":
            dados_do_formulario['dirigente_responsavel'] = st.radio("Assinatura:",("Reitor(a)", "Vice-Reitor(a)"))


        st.write("") # Quebra de linha
        coluna_btn_1, coluna_btn_2, coluna_btn_3 = st.columns([2,3,1])
        with coluna_btn_1:
            pass
        with coluna_btn_2:
            btn_gera_ato = st.form_submit_button('GRAVAR INFORMAÇÕES DO ATO')
            
        with coluna_btn_3:
            pass

    if btn_gera_ato:
        gerar_ato(dados_do_formulario)
        
        

    