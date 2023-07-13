import streamlit as st
import os 
import datetime
from auxiliares.connection import *
import docx
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from auxiliares.var_globais import lista_de_anos, lista_dias_mes, lista_meses_ano


#Baixar Arquivo
def baixar_documento(form_gerado):
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
def gerar_conteudo_publicacao(num_ato, ano_ato, texto): 

    # posicionando inicio do texto
    inicio = texto.find('>') + 1 
    # coletando informações para gravar
    data_atual = data_convertida_br(str(datetime.date.today()))
    _numero_ato_ = f'Nº {num_ato}/{ano_ato}'
    texto_gravar = texto[inicio:].replace('<p style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">', '').replace('</p>', '').lstrip()
    # mostrando texto do ato abaixo do formulário
    texto_print = f"""{_numero_ato_} - {texto_gravar}"""
    texto_publ = {'Texto_para_Publicação': texto_print}
    st.write(texto_publ)
    ato_gravacao = {'data_emissao': data_atual, 'num_formatado': _numero_ato_, 'texto_do_ato_gravar': texto_gravar}
    return ato_gravacao

def gerar_word_publicacao(word_dict, preambulo_doc):
    # Criando documento
    documento = Document()
    # core_properties = documento.core_properties / core_properties.language = "pt-BR" -> não funciona para alterar o idioma e corrigir a verificação ortográfica
    # Copiei a solução do github (link abaixo)
    # https://github.com/python-openxml/python-docx/issues/727  
    for my_style in documento.styles:
        style = documento.styles[my_style.name]
        rpr = style.element.get_or_add_rPr()
        lang = docx.oxml.shared.OxmlElement('w:lang')
        if not rpr.xpath('w:lang'):
            lang.set(docx.oxml.shared.qn('w:val'),'de-DE')
            lang.set(docx.oxml.shared.qn('w:eastAsia'),'en-US')
            lang.set(docx.oxml.shared.qn('w:bidi'),'ar-SA')
            rpr.append(lang)  

    # criando cabeçalho do documento

    dia_do_mes = st.selectbox("Escolha o dia:", lista_dias_mes)
    nome_do_mes = st.selectbox("Escolha o dia:", lista_meses_ano)
    ano_data = st.selectbox("Escolha o dia:", lista_de_anos)

    data_doc_word = f'Brasília, {dia_do_mes} de {nome_do_mes} de {ano_data}\n'
    preambulo_doc_word = preambulo_doc
    documento.add_paragraph(data_doc_word)
    documento.add_paragraph(preambulo_doc_word)

    # Gravando texto e gerando documento
    for posicao in range(len(word_dict['NUMERO'])):
        
        textis = f"{word_dict['NUMERO'][posicao]} - {word_dict['TEXTO'][posicao]}".replace('\n', ' ')
        paragrafo = documento.add_paragraph(textis)
        paragrafo_formatado = paragrafo.paragraph_format
        paragrafo_formatado.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # Salvando documento
    documento.save("AtosPublicacao.docx")
    baixar_documento("AtosPublicacao.docx")


