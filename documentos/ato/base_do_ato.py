import streamlit as st
from documentos.ato.partes_do_ato import *


def gerar_ato(formulario):

    teste_epigarafe = epigrafe_ato(formulario)
    teste_ementa = ementa_ato(formulario)
    # colocar dados em variáveis??
    # Sobrescrever os dados no dicionário dados_do_formulário que precisarem de formatação de strings ou datas
    with open("file.html", "w", encoding='utf-8') as f:
        
        f.write(f'''{teste_epigarafe}
                     {teste_ementa}''') # 

        
        