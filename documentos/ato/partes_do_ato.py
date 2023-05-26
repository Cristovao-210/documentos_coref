import streamlit as st
from auxiliares.tags_html_atos import *


# A epígrafe é a parte do ato que o qualifica na ordem jurídica e o situa no tempo, por meio da
# denominação, da numeração e da data, devendo ser grafadas em maiúsculas e sem ponto final.
# No nosso contexto é o setor responsável pelo ato
# TÍTULO
def epigrafe_ato(informacoes_do_formulario): # setor_responsavel, numero_ato

    if informacoes_do_formulario['setor_responsavel'] == "DGP":
        return f'''<p style="font-size:13pt;font-family:Calibri;text-align:center;text-transform:uppercase;word-wrap:normal;">
                      ATO DO DECANATO DE GESTÃO DE PESSOAS Nº {informacoes_do_formulario['numero_ato']}
	               </p>'''
    elif informacoes_do_formulario['setor_responsavel'] == "DGP/DAP":
        return f'''<p style="font-size:13pt;font-family:Calibri;text-align:center;text-transform:uppercase;word-wrap:normal;">
                      ATO DA DIRETORIA DE ADMINISTRAÇÃO DE PESSOAS Nº {informacoes_do_formulario['numero_ato']}
                   </p>'''
    elif informacoes_do_formulario['setor_responsavel'] == "REITORIA":
         return f'''<p style="font-size:13pt;font-family:Calibri;text-align:center;text-transform:uppercase;word-wrap:normal;">
                      ATO DA REITORIA Nº {informacoes_do_formulario['numero_ato']}
                    </p>'''
    

###########################################################################################################################
# A ementa é a parte do ato que resume o conteúdo do ato normativo para permitir, de
# modo objetivo e claro, o conhecimento da matéria legislada.
# TEXTO ALINHADO A DIREITA ABAIXO DO TÍTULO
def ementa_ato(informacoes_do_formulario):

    # CDS
    if informacoes_do_formulario['tipo_de_ato'] == "Nomeação de CD":
       return f'''{ementa_abre_tag} 

                  {ementa_fecha_tag}'''
    
    elif informacoes_do_formulario['tipo_de_ato'] == "Exoneração de CD":
        return f'''{ementa_abre_tag} 
       
                   {ementa_fecha_tag}'''
    
    elif informacoes_do_formulario['tipo_de_ato'] == "Substitução de CD":
        return f'''{ementa_abre_tag} 
       
                   {ementa_fecha_tag}'''
    
    elif informacoes_do_formulario['tipo_de_ato'] == "Recondução de CD":
        return f'''{ementa_abre_tag} 
       
                   {ementa_fecha_tag}'''
    
    # FGS    
    elif informacoes_do_formulario['tipo_de_ato'] == "Designação de FG":
        return f'''{ementa_abre_tag} 
       
                   {ementa_fecha_tag}'''
    
    elif informacoes_do_formulario['tipo_de_ato'] == "Dispensa de FG":
        return f'''{ementa_abre_tag} 
       
                   {ementa_fecha_tag}'''
    
    elif informacoes_do_formulario['tipo_de_ato'] == "Substitução de FG":
       return f'''{ementa_abre_tag} 
       
                  {ementa_fecha_tag}'''
    
    #FCCS
    elif informacoes_do_formulario['tipo_de_ato'] == "Designação de FCC":
        return f'''{ementa_abre_tag} 
       
                   {ementa_fecha_tag}'''
    
    elif informacoes_do_formulario['tipo_de_ato'] == "Dispensa de FCC":
        return f'''{ementa_abre_tag} 
       
                   {ementa_fecha_tag}'''
    
    elif informacoes_do_formulario['tipo_de_ato'] == "Substitução de FCC":
        return f'''{ementa_abre_tag} 
       
                   {ementa_fecha_tag}'''
    
    elif informacoes_do_formulario['tipo_de_ato'] == "FCC não remunerada":
        return f'''{ementa_abre_tag} 
       
                   {ementa_fecha_tag}'''
    
    else:
        return f'''{ementa_abre_tag} 
                    ERRO: Nenhum Tipo de ato selecionado.
                   {ementa_fecha_tag}'''










#############################################################################################################################
# O preâmbulo contém a declaração do nome da autoridade, do cargo em que se encontra
# investida e da atribuição constitucional em que se funda, quando for o caso, para promulgar o
# ato normativo e a ordem de execução ou mandado de cumprimento, a qual prescreve a força
# coativa do ato normativo.
# TEXTO QUE FALA DA COMPETÊNCIA
def preambulo_ato(informacoes_do_formulario): # setor_responsavel, numero_do_sei
    #Reitoria
    #DGP
    #DGP/DAP
    pass


#############################################################################################################################
# TEXTO DO ATO 
def texto_do_ato(informacoes_do_formulario): # tipo_ato, tipo_funcao
    # tipo_ato = Designação/Nomeação, Dispensa/Exoneração, Substituição
    # tipo_funcao = FCC, FG, CD
    pass


#############################################################################################################################
# Reitora, Vice, decana e decana em exercício
# QUEM VAI ASSINAR
def assinatura_ato(informacoes_do_formulario): # tipo_ato, titularidade 
    #Reitoria
    #DGP
    #DGP/DAP
    pass

