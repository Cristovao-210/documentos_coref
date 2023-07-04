import streamlit as st
import os


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


# gerar word
def gerar_documento_publicacao(num_ato, ano_ato):
    
    _numero_ato_ = f'Nº {num_ato}/{ano_ato}'
    return _numero_ato_
    
    

# função para deixar data recebida no formato necessário
def data_convertida_br(dt): # recebe uma String
  dia = dt[8:]
  mes = dt[5:7]
  ano = dt[0:4]
  if dia == "":
    return ""
  else:
    return f'{dia}/{mes}/{ano}' # retorna uma String
