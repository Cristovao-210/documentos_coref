import streamlit as st
from  documentos.ato.compor_arquivo_atos import *
from auxiliares.funcoes import *

# TÍTULO
def epigrafe_ato(informacoes_do_formulario): # setor_responsavel, numero_ato

    numero_do_ato = f"{informacoes_do_formulario['numero_ato']} / {informacoes_do_formulario['ano_do_ato']}"

    if informacoes_do_formulario['setor_responsavel'] == "DGP":
        return epigrafe['html'].format(epigrafe['txt_dgp'].format(numero_do_ato))
    elif informacoes_do_formulario['setor_responsavel'] == "DGP/DAP":
        return epigrafe['html'].format(epigrafe['txt_dgp_dap'].format(numero_do_ato))
    elif informacoes_do_formulario['setor_responsavel'] == "REITORIA":
        return epigrafe['html'].format(epigrafe['txt_reitoria'].format(numero_do_ato))
    else:
        return epigrafe['html'].format(epigrafe['txt_erro'])

# TEXTO ALINHADO A DIREITA ABAIXO DO TÍTULO
def ementa_ato(informacoes_do_formulario):

    tpd_ato = informacoes_do_formulario['tipo_de_ato']

    # 0-categoria_cargo (o(a) Docente/Servidor(a)/o Professor do Magistério Superior/a Professora do Magistério Superior) 
    categoria_funcional = informacoes_do_formulario['categoria_funcional']
    if categoria_funcional == "Outros (Usar campo 'Nome do Servidor')":
        categoria_funcional = ''
    # 1-nome
    nome_servidor = informacoes_do_formulario['nome_servidor']
    # 2-nome_COORDENAÇÃO/DIREÇÃO, (Coordenador(a) de Pós-graduação/Coordenador(a) de Graduação), 3-descrição do curso a ser coordenado
    nome_da_funcao = f'{informacoes_do_formulario["nome_da_funcao"]} {informacoes_do_formulario["descricao_da_funcao"]}' if informacoes_do_formulario["nome_da_funcao"][0:6] != "Outros" else informacoes_do_formulario["descricao_da_funcao"]
    # 3- cd-1 a 4,fg-1 a 3,fcc
    tipo_de_funcao = informacoes_do_formulario['tipo_de_funcao']
    # quando substituição #['a Coordenadora', 'o Coordenador', 'o Diretor', 'a Diretora', 'outros']
    # if tpd_ato == "Substituição de CD" or tpd_ato == "Substituição de FG" or tpd_ato == "Substituição de FCC":
    #     cargo_a_ser_substituido = informacoes_do_formulario['cargo_a_ser_substituido'] # Concatenar com o nome da função]

    # CDS
    if informacoes_do_formulario['tipo_de_ato'] == "Nomeação de CD":
       return ementa['funcao']['html'].format(ementa['funcao']['txt_cds']['nomeacao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Exoneração de CD":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_cds']['exoneracao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Substituição de CD":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_cds']['substituicao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao)) #cargo_a_ser_substituido
    elif informacoes_do_formulario['tipo_de_ato'] == "Recondução de CD":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_cds']['reconducao'].format(categoria_funcional, nome_servidor, nome_da_funcao)) 
    # FGS    
    elif informacoes_do_formulario['tipo_de_ato'] == "Designação de FG":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_fgs']['designacao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Dispensa de FG":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_fgs']['dispensa'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Substituição de FG":
       return ementa['funcao']['html'].format(ementa['funcao']['txt_fgs']['substituicao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))#cargo_a_ser_substituido
    #FCCS
    elif informacoes_do_formulario['tipo_de_ato'] == "Designação de FCC":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_fccs']['designacao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Dispensa de FCC":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_fccs']['dispensa'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Substituição de FCC":
        return ementa['funcao']['html'].format(ementa['funcao']['txt_fccs']['substituicao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))#cargo_a_ser_substituido
    elif informacoes_do_formulario['tipo_de_ato'] == "FCC não remunerada":
        if informacoes_do_formulario['tipo_de_ato']['tipo_nao_remunerada'] == 'Designação':
            return ementa['funcao']['html'].format(ementa['funcao']['txt_fccs']['nao_remunerada']['designacao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
        else:
            return ementa['funcao']['html'].format(ementa['funcao']['txt_fccs']['nao_remunerada']['dispensa'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    else:
        return ementa['funcao']['html'].format(ementa['funcao']['txt_erro'])

# TEXTO QUE FALA DA COMPETÊNCIA
def preambulo_ato(informacoes_do_formulario): # setor_responsavel, numero_do_sei
    numero_do_sei = informacoes_do_formulario['numero_do_sei']
    if informacoes_do_formulario['setor_responsavel'] == "DGP":
        if informacoes_do_formulario['dirigente_responsavel'] == "Decano(a) titular":
            return preambulo['funcao']['html'].format(preambulo['funcao']['txt_dgp'].format(numero_do_sei))
        else:
            return preambulo['funcao']['html'].format(preambulo['funcao']['txt_dgp_substituto'].format(numero_do_sei))
    elif informacoes_do_formulario['setor_responsavel'] == "DGP/DAP":
        if informacoes_do_formulario['dirigente_responsavel'] == "Diretor(a) titular":
            return preambulo['funcao']['html'].format(preambulo['funcao']['txt_dgp_dap'].format(numero_do_sei))
        else:
            return preambulo['funcao']['html'].format(preambulo['funcao']['txt_dgp_dap_susbstituto'].format(numero_do_sei))
    elif informacoes_do_formulario['setor_responsavel'] == "REITORIA":
        if informacoes_do_formulario['dirigente_responsavel'] == "Reitor(a)":
            return preambulo['funcao']['html'].format(preambulo['funcao']['txt_reitoria'].format(numero_do_sei))
        else:
            return preambulo['funcao']['html'].format(preambulo['funcao']['txt_reitoria_substituto'].format(numero_do_sei))
    else:
        return preambulo['funcao']['html'].format(preambulo['funcao']['txt_erro'].format(numero_do_sei))
    
#############################################################################################################################
# TEXTO DO ATO 

def texto_do_ato(informacoes_do_formulario): # tipo_ato, tipo_funcao

    tpd_ato = informacoes_do_formulario['tipo_de_ato']
    #carg_vag = informacoes_do_formulario['cargo_vago']
    # 0-categoria_cargo (o(a) Docente/Servidor(a)/o Professor do Magistério Superior/a Professora do Magistério Superior) 
    categoria_funcional = informacoes_do_formulario['categoria_funcional']
    if categoria_funcional == "Outros (Usar campo 'Nome do Servidor')":
        categoria_funcional = ''
    # 1-nome
    nome_servidor = informacoes_do_formulario['nome_servidor']
    # 2-nome_COORDENAÇÃO/DIREÇÃO, (Coordenador(a) de Pós-graduação/Coordenador(a) de Graduação), 3-descrição do curso a ser coordenado
    nome_da_funcao = f'{informacoes_do_formulario["nome_da_funcao"]} {informacoes_do_formulario["descricao_da_funcao"]}' if informacoes_do_formulario["nome_da_funcao"][0:6] != "Outros" else informacoes_do_formulario["descricao_da_funcao"]
    # 3- cd-1 a 4,fg-1 a 3,fcc
    tipo_de_funcao = informacoes_do_formulario['tipo_de_funcao']

    if tpd_ato == "Substituição de CD" or tpd_ato == "Substituição de FG" or tpd_ato == "Substituição de FCC":
        # quando substituição #['a Coordenadora', 'o Coordenador', 'o Diretor', 'a Diretora', 'outros']
        motivo_do_afastamento = informacoes_do_formulario['motivo_do_afastamento']
        #cargo_a_ser_substituido = informacoes_do_formulario['cargo_a_ser_substituido'] # Concatenar com o nome da função]
        dt_inicial_substituicao = data_convertida_br(str(informacoes_do_formulario['data_inicial_substuicao']))
        dt_final_substituicao = data_convertida_br(str(informacoes_do_formulario['data_final_substuicao']))
        servidor_a_ser_substituido = informacoes_do_formulario['servidor_a_ser_substituido']

        
    # detalhe em nomeação de cd
    if tpd_ato == "Nomeação de CD":
        genero = informacoes_do_formulario['genero']
        ja_tem_funcao = ""
        if genero == "Masculino":
            ja_tem_funcao = ', dispensando-o da função que atualmente ocupa.'
        elif genero == "Feminino":
            ja_tem_funcao = ', dispensando-a da função que atualmente ocupa.'
        else:
            ja_tem_funcao = '.'

    # detalhe em exoneração de cd - parte final do texto
    if tpd_ato == "Exoneração de CD":
        termino = informacoes_do_formulario['termino_de_mandato']
        if termino == "Sim":
            termino_de_mandato = ' , por término de mandato.'
        else:
            termino_de_mandato = '.'

        if tpd_ato == "Recondução de CD":
            data_reconducao = data_convertida_br(str(informacoes_do_formulario['data_reconducao']))

    # CDS
    if informacoes_do_formulario['tipo_de_ato'] == "Nomeação de CD":
       return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_cds']['nomeacao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao,
                                                                                                    ja_tem_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Exoneração de CD":
        return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_cds']['exoneracao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao, termino_de_mandato))
    
    elif informacoes_do_formulario['tipo_de_ato'] == "Substituição de CD":
        if informacoes_do_formulario['cargo_vago'] == "Sim":
            return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_cds']['substituicao_vago'].format(categoria_funcional, nome_servidor, nome_da_funcao,
                                                                                    tipo_de_funcao, motivo_do_afastamento, dt_inicial_substituicao, 
                                                                                    dt_final_substituicao))# cargo_a_ser_substituido
        else:
            return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_cds']['substituicao'].format(categoria_funcional, nome_servidor, nome_da_funcao,
                                                                                                         tipo_de_funcao, motivo_do_afastamento,
                                                                                                         dt_inicial_substituicao, dt_final_substituicao, servidor_a_ser_substituido))    
    elif informacoes_do_formulario['tipo_de_ato'] == "Recondução de CD":
        return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_cds']['reconducao'].format(categoria_funcional, nome_servidor, nome_da_funcao,
                                                                                                       tipo_de_funcao, data_reconducao)) 
    # FGS    
    elif informacoes_do_formulario['tipo_de_ato'] == "Designação de FG":
        return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_fgs']['designacao'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Dispensa de FG":
        return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_fgs']['dispensa'].format(categoria_funcional, nome_servidor, nome_da_funcao, tipo_de_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Substituição de FG":
       if informacoes_do_formulario['cargo_vago'] == "Sim":
        return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_fgs']['substituicao_vago'].format(categoria_funcional, nome_servidor, nome_da_funcao,
                                                                                                        tipo_de_funcao, motivo_do_afastamento, dt_inicial_substituicao,
                                                                                                        dt_final_substituicao))
       else:
        return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_fgs']['substituicao'].format(categoria_funcional, nome_servidor, nome_da_funcao,
                                                                                                        tipo_de_funcao, motivo_do_afastamento, dt_inicial_substituicao,
                                                                                                        dt_final_substituicao, servidor_a_ser_substituido))
           
    #FCCS
    elif informacoes_do_formulario['tipo_de_ato'] == "Designação de FCC":
        return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_fccs']['designacao'].format(categoria_funcional, nome_servidor, nome_da_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Dispensa de FCC":
        return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_fccs']['dispensa'].format(categoria_funcional, nome_servidor, nome_da_funcao))
    elif informacoes_do_formulario['tipo_de_ato'] == "Substituição de FCC":
        if informacoes_do_formulario['cargo_vago'] == "Sim":
            return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_fccs']['substituicao_vago'].format(categoria_funcional, nome_servidor, nome_da_funcao,
                                                                                                         motivo_do_afastamento, dt_inicial_substituicao,
                                                                                                         dt_final_substituicao))
        else:
            return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_fccs']['substituicao'].format(categoria_funcional, nome_servidor, nome_da_funcao,
                                                                                                         motivo_do_afastamento, dt_inicial_substituicao,
                                                                                                         dt_final_substituicao, servidor_a_ser_substituido))

    elif informacoes_do_formulario['tipo_de_ato'] == "FCC não remunerada":
        if informacoes_do_formulario['tipo_de_ato']['tipo_nao_remunerada'] == 'Designação':
            return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_fccs']['nao_remunerada']['designacao'].format(categoria_funcional, nome_servidor, nome_da_funcao))
        else:
            return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_fccs']['nao_remunerada']['dispensa'].format(categoria_funcional, nome_servidor, nome_da_funcao))
    else:
        return texto_ato['funcao']['html'].format(texto_ato['funcao']['txt_erro'])
    

#############################################################################################################################
# QUEM VAI ASSINAR
def assinatura_ato(informacoes_do_formulario): # tipo_ato, titularidade 
    
    dirigente_responsavel = informacoes_do_formulario['dirigente_responsavel']
    
    if dirigente_responsavel == "Decano(a) titular":
        return dirigentes['html'].format(dirigentes['dgp']['decanato']['titular'])
    elif dirigente_responsavel == "Decano(a) em exercício":
        return dirigentes['html'].format(dirigentes['dgp']['decanato']['em_exercicio'])
    elif dirigente_responsavel == "Diretor(a) titular":
        return dirigentes['html'].format(dirigentes['dgp']['dap']['titular'])
    elif dirigente_responsavel == "Diretor(a) em exercício":
        return dirigentes['html'].format(dirigentes['dgp']['dap']['em_exercicio'])
    elif dirigente_responsavel == "Reitor(a)":
        return dirigentes['html'].format(dirigentes['reitoria']['titular'])
    elif dirigente_responsavel == "Vice-Reitor(a)":
        return dirigentes['html'].format(dirigentes['reitoria']['em_exercicio'])
    else:
        return dirigentes['html'].format('Nenhum dirigente selecionado')

