import streamlit as st

# criando conexão
def criar_conexao(_nome_do_banco_): # 'atosgerados_db'
    conn = st.experimental_connection(_nome_do_banco_, type='sql')
    return conn

#criar tabela
def criar_db(conexao):
    with conexao.session as s:
        s.execute('''CREATE TABLE IF NOT EXISTS atos_publicacao (
                    id_ato int NOT NULL, 
                    data_emissao VARCHAR(10),
                    numero_formatado VARCHAR(20),
                    texto_do_ato VARCHAR(1000));''')

# salvar atos na tabela        
def inserir_atos(conexao, tabela, base_dados):
    with conexao.session as s:
        for dado in base_dados:
            s.execute(
                f'INSERT INTO {tabela} (data_emissao, numero_formatado, texto_do_ato) VALUES (%s, %s, %s);',
                params=base_dados[dado]
            )
        s.commit()

# buscar atos na tabela
def selecionar_atos(conexao, tabela, dt_emissao):
    # listar atos
    with conexao.session as s:
        dict_atos = s.execute(f'select * from {tabela} where data_emissao = {dt_emissao}')
        st.dataframe(dict_atos)
    
    # gerar word
        