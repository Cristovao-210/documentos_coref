


###########################################################################################################################
# BASE DO ATO

documento_base = {}

###########################################################################################################################
# EPIGRAFE
epigrafe = {
            
    'html': '<p style="font-size:13pt;font-family:Calibri;text-align:center;text-transform:uppercase;word-wrap:normal;">{0}</p>',
    'txt_dgp': 'ATO DO DECANATO DE GESTÃO DE PESSOAS Nº {0}',
    'txt_dgp_dap':'ATO DA DIRETORIA DE ADMINISTRAÇÃO DE PESSOAS Nº {0}',
    'txt_reitoria':'ATO DA REITORIA Nº {0}',
    'txt_erro': 'ERRO: NENHUM SETOR RESPONSÁVEL SELECIONADO'

}
#teste_epigaraf = epigrafe['html'].format(epigrafe['txt_reitoria'].format('2012/2023'))

###########################################################################################################################
# EMENTA

ementa = {

    'html': '''
        <table cellpadding="1" cellspacing="1" style="margin-left: auto; margin-right: 3pt; width: 795px;">
            <tbody>
                <tr>
                    <td style="width: 403px; text-align: left;">&nbsp;</td>
                    <td style="width: 379px; text-align: left;">
                        <p style="font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;">
                        {0}
                        </p>
                    </td>
                </tr>
            </tbody>
        </table> ''',
    'txt_cds': {    
        # 0-categoria_cargo (docente/servidor) 1-nome, 2-nome_funcao, 3-numero_cd
        'nomeacao': 'Nomeia {0} {1} para exercer a função de {2} ({3}).', 
        # 0-categoria_cargo (docente/servidor) 1-nome, 2-nome_funcao, 3-numero_cd
        'exoneracao': 'Exonera {0} {1} da função de {2} ({3}).', 
        # 0-categoria_cargo (docente/servidor) 1-nome, 2-nome_COORDENAÇÃO/DIREÇÃO, 3-numero_cd
        'substituicao':'Nomeia {0} {1} para substituir a {2} ({3}).', 
        # 0-categoria_cargo (docente/servidor) 1-nome, 2-nome_funcao
        'reconducao':'Reconduz {0} {1} para exercer a função de {2}.' 
    },
    'txt_fgs': {
        'designacao': '',
        'dispensa': '',
        'substituicao': ''
    },
    'txt_fccs': {
        'designacao': '',
        'dispensa': '',
        'substituicao': '',
        'nao_remunerada': ''
    },
    'txt_erro': 'ERRO: Nenhum Tipo de ato selecionado.'

}
#teste_ementa = ementa['html'].format(ementa['txt_cds']['nomeacao'].format('o servidor', 'Márcio Cristóvão', 'Coordenador do tempo', 'CD-04'))


###########################################################################################################################

###########################################################################################################################

###########################################################################################################################

###########################################################################################################################




# with open("file.html", "w", encoding='utf-8') as f:
#     f.write(f'{teste_epigaraf} {teste_ementa}')



