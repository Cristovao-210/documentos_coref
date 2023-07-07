import streamlit as st
import os 
import datetime
from auxiliares.connection import *


#Baixar Arquivo
def baixar_formulario(form_gerado):
    st.markdown('<p style="text-align: center; background: lightgreen">Clique no botão abaixo para fazer download do documento</p>', unsafe_allow_html=True)
    pos_btn_1, pos_btn_2, pos_btn_3 = st.columns([3,3,2])
    with pos_btn_1:
        pass
    with pos_btn_2:
       try:
            with open(str(form_gerado), "rb") as file:
                st.download_button(
                    label="BAIXAR DOCUMENTO",
                    data=file,
                    file_name=form_gerado,
                    mime="text/html")
       except:
            st.error("ARQUIVO NÃO LOCALIZADO! REPITA O PROCESSO.")
    with pos_btn_3:
        pass
    os.remove(form_gerado)
   
# função para deixar data recebida no formato necessário
def data_convertida_br(dt): # recebe uma String
  dia = dt[8:]
  mes = dt[5:7]
  ano = dt[0:4]
  if dia == "":
    return ""
  else:
    return f'{dia}/{mes}/{ano}' # retorna uma String
  
# gerar word
def gerar_documento_publicacao(num_ato, ano_ato, texto): 

    # posicionando inicio do texto
    inicio = texto.find('>') + 1 
    # coletando informações para gravar
    data_atual = data_convertida_br(str(datetime.date.today()))
    _numero_ato_ = f'Nº {num_ato}/{ano_ato}'
    texto_gravar = texto[inicio:].replace('</p>', '').lstrip()
    # mostrando texto do ato abaixo do formulário
    texto_print = f"""{_numero_ato_} - {texto[inicio:].replace('</p>', '').lstrip()}"""
    texto_publ = {'Texto_para_Publicação': texto_print}
    st.write(texto_publ)
    ato_gravacao = {'data_emissao': data_atual, 'num_formatado': _numero_ato_, 'texto_do_ato_gravar': texto_gravar}
    return ato_gravacao
    

