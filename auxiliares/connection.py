import streamlit as st
import pandas as pd

# criando conexão
def criar_conexao(_nome_do_banco_): # 'atosgerados_db'
    try:
        conn = st.experimental_connection(_nome_do_banco_, type='sql')
        return conn
    except:
        st.error('Erro na criação do Banco de Dados')

#criar tabela
def criar_tabela(conexao):
    with conexao.session as s:
        s.execute('''CREATE TABLE IF NOT EXISTS atos_publicacao (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    dataemissao VARCHAR(10),
                    numeroformatado VARCHAR(20),
                    textodoato VARCHAR(1000))''')

# salvar atos na tabela        
def inserir_atos(conexao, tabela, base_dados):
    data, numero, texto = base_dados["data_emissao"], base_dados["num_formatado"], base_dados["texto_do_ato_gravar"]
    with conexao.session as s:
        
        s.execute(f'''INSERT INTO {tabela} (dataemissao, numeroformatado, textodoato) VALUES (:data, :numero, :texto)''',
                   params=dict(data=data, numero=numero, texto=texto))
        s.commit()

# buscar atos na tabela
def selecionar_atos(conexao, tabela, dt_emissao):# , 
    # listar atos
    with conexao.session as s:
        dict_atos = s.execute(f'SELECT dataemissao AS EMISSAO, numeroformatado AS NUMERO, textodoato AS TEXTO from {tabela} where dataemissao = "{dt_emissao}"')
        df = pd.DataFrame(dict_atos)
        indice_vazio = [''] * len(df)
        df.index = indice_vazio
        return df
        
        

        
    
    # gerar word
        