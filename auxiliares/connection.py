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
                    dirigente_responsavel VARCHAR(200),
                    setor_responsavel VARCHAR(400),
                    dataemissao VARCHAR(10),
                    numeroformatado VARCHAR(20),
                    textodoato VARCHAR(1000))''')

# salvar atos na tabela        
def inserir_atos(conexao, tabela, base_dados):
    dirigente, setor, data, numero, texto = base_dados["dirigente_responsavel"], base_dados["setor_responsavel"], base_dados["data_emissao"], base_dados["num_formatado"], base_dados["texto_do_ato_gravar"]
    with conexao.session as s:
        
        s.execute(f'''INSERT INTO {tabela} (dirigente_responsavel, setor_responsavel, dataemissao, numeroformatado, textodoato) VALUES (:dirigente, :setor, :data, :numero, :texto)''',
                   params=dict(dirigente=dirigente, setor=setor, data=data, numero=numero, texto=texto))
        s.commit()

# buscar atos na tabela
def selecionar_atos(conexao, tabela, dt_emissao):# , 
    # listar atos
    with conexao.session as s:
        dict_atos = s.execute(f'SELECT dirigente_responsavel AS DIRIGENTE, setor_responsavel AS SETOR, dataemissao AS EMISSAO, numeroformatado AS NUMERO, textodoato AS TEXTO from {tabela} where dataemissao = "{dt_emissao}"')
        df = pd.DataFrame(dict_atos)
        indice_vazio = [''] * len(df)
        df.index = indice_vazio

        return df
        
        

        
    
    # gerar word
        