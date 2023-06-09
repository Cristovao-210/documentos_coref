import streamlit as st
from  documentos.ato.compor_arquivo_atos import *


# TÍTULO
def epigrafe_ato(informacoes_do_formulario): # setor_responsavel, numero_ato

    numero_do_ato = informacoes_do_formulario['numero_ato']
    if informacoes_do_formulario['setor_responsavel'] == "DGP":
        return epigrafe['html'].format(epigrafe['txt_dgp'].format(numero_do_ato))
    elif informacoes_do_formulario['setor_responsavel'] == "DGP/DAP":
        return epigrafe['html'].format(epigrafe['txt_dgp_dap'].format(numero_do_ato))
    elif informacoes_do_formulario['setor_responsavel'] == "REITORIA":
        return epigrafe['html'].format(epigrafe['txt_reitoria'].format(numero_do_ato))
    else:
        return epigrafe['html'].format(epigrafe['txt_erro'])
    
###########################################################################################################################
# TEXTO ALINHADO A DIREITA ABAIXO DO TÍTULO
def ementa_ato(informacoes_do_formulario):

    # 0-categoria_cargo (o(a) Docente/Servidor(a)/o Professor do Magistério Superior/a Professora do Magistério Superior) 
    categoria_funcional = informacoes_do_formulario['categoria_funcional']
    # 1-nome
    nome_servidor = informacoes_do_formulario['nome_servidor']
    # 2-nome_COORDENAÇÃO/DIREÇÃO, (Coordenador(a) de Pós-graduação/Coordenador(a) de Graduação), 3-descrição do curso a ser coordenado
    nome_da_funcao = informacoes_do_formulario['nome_da_funcao']
    # 3- cd-1 a 4,fg-1 a 3,fcc
    tipo_de_funcao = informacoes_do_formulario['tipo_de_funcao'] 
    # quando substituição #['a Coordenadora', 'o Coordenador', 'o Diretor', 'a Diretora', 'outros']
    cargo_a_ser_substituido = informacoes_do_formulario['cargo_a_ser_substituido'] # Concatenar com o nome da função]

    # CDS
    if informacoes_do_formulario['tipo_de_ato'] == "Nomeação de CD":
       return ementa['funcao']['html'].format(ementa['funcao']['txt_cds']['nomeacao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Exoneração de CD":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_cds']['exoneracao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Substitução de CD":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_cds']['substituicao'].format(categoria_funcional, nome_servidor, cargo_a_ser_substituido, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Recondução de CD":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_cds']['reconducao'].format(categoria_funcional, nome_servidor, nome_da_funcao))
            
    # FGS    
    elif informacoes_do_formulario['tipo_de_ato'] == "Designação de FG":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_fgs']['designacao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Dispensa de FG":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_fgs']['dispensa'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Substitução de FG":
       return ementa['funcao']['html'].format(ementa['funcao']['txt_fgs']['substituicao'].format(categoria_funcional, nome_servidor, cargo_a_ser_substituido, tipo_de_funcao))
    
    #FCCS
    elif informacoes_do_formulario['tipo_de_ato'] == "Designação de FCC":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_fccs']['designacao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Dispensa de FCC":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_fccs']['dispensa'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Substitução de FCC":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_fccs']['substituicao'].format(categoria_funcional, nome_servidor, cargo_a_ser_substituido, tipo_de_funcao))   
    elif informacoes_do_formulario['tipo_de_ato'] == "FCC não remunerada":
        if informacoes_do_formulario['tipo_de_ato']['tipo_nao_remunerada'] == 'Designação':
            return ementa['funcao']['html'].format(ementa['funcao']['txt_fccs']['nao_remunerada']['designacao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
        else:
            return ementa['funcao']['html'].format(ementa['funcao']['txt_fccs']['nao_remunerada']['dispensa'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    else:
        return ementa['funcao']['html'].format(ementa['funcao']['txt_erro'])

#############################################################################################################################
# TEXTO QUE FALA DA COMPETÊNCIA
def preambulo_ato(informacoes_do_formulario): # setor_responsavel, numero_do_sei

    numero_do_sei = informacoes_do_formulario['numero_do_sei']

    if informacoes_do_formulario['setor_responsavel'] == "DGP":
        return preambulo['funcao']['html'].format(preambulo['funcao']['txt_dgp'].format(numero_do_sei))
    elif informacoes_do_formulario['setor_responsavel'] == "DGP/DAP":
        return preambulo['funcao']['html'].format(preambulo['funcao']['txt_dgp_dap'].format(numero_do_sei))
    elif informacoes_do_formulario['setor_responsavel'] == "REITORIA":
        return preambulo['funcao']['html'].format(preambulo['funcao']['txt_reitoria'].format(numero_do_sei))
    else:
        return preambulo['funcao']['html'].format(preambulo['funcao']['txt_erro'].format(numero_do_sei))
    


#############################################################################################################################
# TEXTO DO ATO 
def texto_do_ato(informacoes_do_formulario): # tipo_ato, tipo_funcao
    # tipo_ato = Designação/Nomeação, Dispensa/Exoneração, Substituição
    # tipo_funcao = FCC, FG, CD
    pass


#############################################################################################################################
# QUEM VAI ASSINAR
def assinatura_ato(informacoes_do_formulario): # tipo_ato, titularidade 
    #Reitoria
    #DGP
    #DGP/DAP
    pass

