import streamlit as st
import os

def verificar_conteudo_str(conteudo_str):
    try:
        if conteudo_str != "" or conteudo_str != None:
            return conteudo_str
    except:
        return ""

#Baixar Arquivo
def baixar_formulario(form_gerado):
    pos_btn_1, pos_btn_2, pos_btn_3 = st.columns([3,3,1])
    with pos_btn_1:
        pass
    with pos_btn_2:
       try:
            with open(str(form_gerado[0]), "rb") as file:
                st.download_button(
                    label="BAIXAR DOCUMENTO",
                    data=file,
                    file_name=form_gerado[0],
                    mime="text/html")
       except:
            st.error("ARQUIVO NÃO LOCALIZADO! REPITA O PROCESSO.")
    with pos_btn_3:
        pass
    os.remove(form_gerado[0])
    

# função para deixar data recebida no formato necessário
def data_convertida_br(dt): # recebe uma String
  dia = dt[8:]
  mes = dt[5:7]
  ano = dt[0:4]
  if dia == "":
    return ""
  else:
    return f'{dia}/{mes}/{ano}' # retorna uma String
