import streamlit as st
from auxiliares.var_globais import *
from documentos.ato.base_do_ato import gerar_ato



def formulario_gerar_ato(dados_do_formulario):

    setor_responsavel = dados_do_formulario['setor_responsavel']
    tp_ato = dados_do_formulario["tipo_de_ato"]

    # em caso de substituição de cargo vago
    if tp_ato == "Substituição de CD" or tp_ato == "Substituição de FG" or tp_ato == "Substituição de FCC":
        cargo_vago = dados_do_formulario['cargo_vago']
        cp_nome_servidor = "Nome do Substituto"
        if cargo_vago == "Sim":
            is_cg_vago =' durante o período de vacância da função gratificada'
            desabilita_nome_titular = True
            a_func_de = 'a função de'
        else:
            is_cg_vago = ''
            desabilita_nome_titular = False
            a_func_de = ''
    else:
        is_cg_vago = ''
        desabilita_nome_titular = False
        a_func_de = ''
        cargo_vago = ''
        cp_nome_servidor = "Nome do Servidor"

    with st.form('form_ato', clear_on_submit=True):

        coluna_1, coluna_2 = st.columns(2)
        with coluna_1:
            dados_do_formulario['numero_ato'] = st.text_input('Informe o número do Ato')
            dados_do_formulario['numero_do_sei'] = st.text_input('Informe o número do Processo SEI')
            dados_do_formulario['nome_servidor'] = st.text_input(cp_nome_servidor)
            dados_do_formulario['descricao_da_funcao'] = st.text_input("Descrição da função", placeholder="Ex: da Faculdade de Tecnologia", value=a_func_de)
      
        with coluna_2:
            dados_do_formulario['ano_do_ato'] = st.text_input('Ano do Ato', value=ano_atual)
            dados_do_formulario['categoria_funcional'] = st.selectbox("Catergoria Funcional", lista_de_categorias_funcionais)
            # verificando se é cargo vago ou não para saber se precisa da lista de nomes da função ou não.
            if "Substituição" in tp_ato and cargo_vago == "Sim":
                dados_do_formulario['nome_da_funcao'] = st.selectbox("Nome da Função", lista_de_nome_funcoes_generos, disabled=True)
            elif "Substituição" in tp_ato and cargo_vago == "Não":
                dados_do_formulario['nome_da_funcao'] = st.selectbox("Nome da Função", lista_de_nome_funcoes_generos)
            elif "Substituição de FCC" in tp_ato:
                dados_do_formulario['nome_da_funcao'] = st.selectbox("Nome da Função", lista_de_nome_funcoes_generos)
            else:
                dados_do_formulario['nome_da_funcao'] = st.selectbox("Nome da Função", lista_de_nome_funcoes)     
            if "CD" in tp_ato:
                dados_do_formulario['tipo_de_funcao'] = st.selectbox("Tipo de Função", dict_de_tipos_funcoes.get('cds'))
            elif "FG" in tp_ato:
                dados_do_formulario['tipo_de_funcao'] = st.selectbox("Tipo de Função", dict_de_tipos_funcoes.get('fgs'))
            elif "FCC" in tp_ato:
                dados_do_formulario['tipo_de_funcao'] = st.selectbox("Tipo de Função", dict_de_tipos_funcoes.get('fccs'))
            
        # SUBSTITUIÇÃO / RECONDUÇÃO
        if tp_ato == "Substituição de CD" or tp_ato == "Substituição de FG" or tp_ato == "Substituição de FCC":            
            dados_do_formulario['motivo_do_afastamento'] = st.text_input("Durante o período de: ", value=is_cg_vago, placeholder="Ex.: durante o período de Férias, Licença Capacitação, etc")
            dados_do_formulario['servidor_a_ser_substituido'] = st.text_input("Nome do Titular a ser substituído: ", disabled=desabilita_nome_titular, value='')
            if is_cg_vago == '':
                dados_do_formulario['do_da_titular'] = st.radio("Definir Gênero: ", ('do titular', 'da titular'))            
                dados_do_formulario['servidor_a_ser_substituido'] = f"{dados_do_formulario['do_da_titular']} {dados_do_formulario['servidor_a_ser_substituido'].title().replace(' Da ', ' da ').replace(' Do ', ' do ').replace(' De ', ' de ').replace(' Di ', ' di ').replace(' Du ', ' du ' )}"
            dados_do_formulario['data_inicial_substuicao'] = st.date_input("Início da Substituição: ")
            dados_do_formulario['data_final_substuicao'] = st.date_input("Término da Substituição: ")
            dados_do_formulario['genero'] = "Masculino"
         # Recondução
        elif tp_ato == "Recondução de CD":        
            dados_do_formulario['data_reconducao'] = st.date_input("Início da Recondução: ")

        # ASSINATURA DO ATO
        if setor_responsavel == "DGP":
            dados_do_formulario['dirigente_responsavel'] = st.radio("Assinatura:",("Decano(a) titular", "Decano(a) em exercício"))
        elif setor_responsavel == "DGP/DAP":
            dados_do_formulario['dirigente_responsavel'] = st.radio("Assinatura:",("Diretor(a) titular", "Diretor(a) em exercício"))
        elif setor_responsavel == "REITORIA":
            dados_do_formulario['dirigente_responsavel'] = st.radio("Assinatura:",("Reitor(a)", "Vice-Reitor(a)"))

        # Quebra de linha / botão para gravar informações
        st.write("") 

        # Botão para gerar documento
        coluna_btn_1, coluna_btn_2, coluna_btn_3 = st.columns([2,3,1])
        with coluna_btn_1:
            pass
        with coluna_btn_2:
            btn_gera_ato = st.form_submit_button('GRAVAR INFORMAÇÕES DO ATO')
        with coluna_btn_3:
            pass

    # Verificando o clique
    if btn_gera_ato:
        gerar_ato(dados_do_formulario)
        
        

    