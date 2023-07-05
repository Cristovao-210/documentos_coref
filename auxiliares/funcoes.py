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
def gerar_documento_publicacao(num_ato, ano_ato, texto):
    
    _numero_ato_ = f'Nº {num_ato}/{ano_ato}'
    inicio = texto.find('>') + 1
    texto_print = f"""{_numero_ato_} - {texto[inicio:].replace('</p>', '').lstrip()}"""
    texto_publ = {'Texto_para_Publicação': texto_print}
    st.write(texto_publ)  #['Texto_Publicação']
    with open('atos_gerados.txt', 'a', encoding='utf-8') as a:
        a.write(f"{texto_publ['Texto_para_Publicação']}\n")
    
    
    

# função para deixar data recebida no formato necessário
def data_convertida_br(dt): # recebe uma String
  dia = dt[8:]
  mes = dt[5:7]
  ano = dt[0:4]
  if dia == "":
    return ""
  else:
    return f'{dia}/{mes}/{ano}' # retorna uma String
