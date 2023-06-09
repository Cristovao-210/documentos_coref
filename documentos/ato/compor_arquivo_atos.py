
################################################### ATOS DE FUNÇÃO ############################################################

# BASE DO ATO

documento_base = {}

#==============================================================================================================================
# EPIGRAFE
epigrafe = {
            
    'html': '<p style="font-size:13pt;font-family:Calibri;text-align:center;text-transform:uppercase;word-wrap:normal;">{0}</p>',
    'txt_dgp': 'ATO DO DECANATO DE GESTÃO DE PESSOAS Nº {0}',
    'txt_dgp_dap':'ATO DA DIRETORIA DE ADMINISTRAÇÃO DE PESSOAS Nº {0}',
    'txt_reitoria':'ATO DA REITORIA Nº {0}',
    'txt_erro': 'ERRO: NENHUM SETOR RESPONSÁVEL SELECIONADO'

}
#teste_epigaraf = epigrafe['html'].format(epigrafe['txt_reitoria'].format('2012/2023'))

#==============================================================================================================================
# EMENTA

ementa = {

    'funcao':{
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
            # 0-categoria_cargo (docente/servidor) 1-nome, 2-nome_COORDENAÇÃO/DIREÇÃO, 3-numero_cd
            'nomeacao': 'Nomeia {0} {1} para exercer a função de {2} ({3}).', 
            'exoneracao': 'Exonera {0} {1} da função de {2} ({3}).', 
            'substituicao':'Nomeia {0} {1} para substituir {2} ({3}).', #['a Coordenadora', 'o Coordenador', 'o Diretor', 'a Diretora', 'outros']
            # 0-categoria_cargo (docente/servidor) 1-nome, 2-nome_funcao
            'reconducao':'Reconduz {0} {1} para exercer a função de {2}.' 
        },
        'txt_fgs': {
            # 0-categoria_cargo (docente/servidor) 1-nome, 2-nome_funcao, 3-numero_fg
            'designacao': 'Designa {0} {1} para exercer a função de {2} ({3}).',
            'dispensa': 'Dispensa {0} {1} da função de {2} ({3}).',
            'substituicao': 'Designa {0} {1} para substituir {2} ({3}).' #['a Coordenadora', 'o Coordenador', 'o Diretor', 'a Diretora', 'outros']
        },
        'txt_fccs': {
            # 0-Genero do Cargo (o Professor do Magistério Superior/a Professora do Magistério Superior) 
            # 1-nome, 2-(Coordenador(a) de Pós-graduação/Coordenador(a) de Graduação), 3-descrição do curso a ser coordenado
            'designacao': 'Designa {0} {1} para exercer a função de {2} em/do {3} (FCC).',
            'dispensa': 'Dispensa {0} {1} da função de {2} em/do {3} (FCC).',
            'substituicao': 'Designa {0} {1} para substituir {2} em/do {3} (FCC).',
            'nao_remunerada': {
                'designacao':'Designa {0} {1} para exercer a função não remunerada de {2} em/do {3}.', # em/do -> colocar no campo de descrição do curso
                'dispensa': 'Dispensa {0} {1} da função não remunerada de {2} em/do {3}.'
            }
        },
        'txt_erro': 'ERRO: Nenhum Tipo de ato selecionado.'
    }    
}
#teste_ementa = ementa['funcao']['html'].format(ementa['funcao']['txt_erro'])
# ementa['funcao']['html'].format(ementa['funcao']['txt_fgs']['substituicao'].format('a Docente', 'Maria Lúcia', 'Menina linda', 'FG-03'))
 
#==============================================================================================================================
preambulo = {

    'funcao':{
        'html': '''
            <p style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">
                {0}
            </p> ''',
        'txt_dgp': '''A DECANA DE GESTÃO DE PESSOAS DA UNIVERSIDADE DE BRASÍLIA, 
                    no uso de suas atribuições legais, conferidas pelo Ato da Reitoria nº .72,
                    publicado no DOU n. 13, de 20 de janeiro de 2021, seção 2, página 24,
                    e de acordo com a competência que lhe foi delegada por meio do Ato da Reitoria n. 304,
                    de 23 de março de 2017, publicado no DOU n. 58, de 24 de março de 2017 
                    e à vista do constante no Processo Eletrônico nº  {0},''',
        'txt_dgp_dap': '''O DIRETOR DE ADMINISTRAÇÃO DE PESSOAS DO DECANATO DE GESTÃO DE PESSOAS DA UNIVERSIDADE DE BRASÍLIA,
                       no uso de suas atribuições legais e de acordo com a competência que lhe foi delegada
                       por meio do Ato do Decanato de Gestão de Pessoas n. 1.593, de 03 de abril de 2017,
                       publicado no DOU n. 66, de 05 de abril de 2017 e à vista do constante no Processo Eletrônico nº {0},''',
        'txt_reitoria': 'A REITORA DA UNIVERSIDADE DE BRASÍLIA, no uso de suas atribuições e considerando o constante no Processo nº {0},',
        'txt_erro': 'ERRO: Nenhum Tipo de Setor Responsável selecionado.'
    }    
} # setor_responsavel, numero_do_sei #Reitoria #DGP  #DGP/DAP
    
    
   
#==============================================================================================================================

#==============================================================================================================================

#==============================================================================================================================




# with open("file.html", "w", encoding='utf-8') as f:
#     f.write(f'{teste_epigaraf} {teste_ementa}')



