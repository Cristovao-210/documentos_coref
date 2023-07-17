
################################################### ATOS DE FUNÇÃO ############################################################
epigrafe = {
    
    'html': '<p style="font-size:13pt;font-family:Calibri;text-align:center;text-transform:uppercase;word-wrap:normal;">{0}</p>',
    'txt_dgp': 'ATO DO DECANATO DE GESTÃO DE PESSOAS Nº {0}',
    'txt_dgp_dap':'ATO DA DIRETORIA DE ADMINISTRAÇÃO DE PESSOAS Nº {0}',
    'txt_reitoria':'ATO DA REITORIA Nº {0}',
    'txt_erro': 'ERRO: NENHUM SETOR RESPONSÁVEL SELECIONADO'

}
#==============================================================================================================================
ementa = {

    'funcao':{
        'html': '''
            <table cellpadding="1" cellspacing="1" style="margin-left: auto; margin-right: 3pt; width: 795px;">
                <tbody>
                    <tr>
                        <td style="width: 403px; text-align: left;">&nbsp;</td>
                        <td style="width: 379px; text-align: left;">
                            <p style="font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;">{0}</p>
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
            'designacao': 'Designa {0} {1} para exercer a função de {2} ({3}).', #  em/do 
            'dispensa': 'Dispensa {0} {1} da função de {2} ({3}).', #em/do 
            'substituicao': 'Designa {0} {1} para substituir {2} ({3}).',# em/do 
            'nao_remunerada': {
                'designacao':'Designa {0} {1} para exercer a função não remunerada de {2}.', # em/do -> colocar no campo de descrição do curso
                'dispensa': 'Dispensa {0} {1} da função não remunerada de {2}.'
            }
        },
        'txt_erro': 'ERRO: Nenhum Tipo de ato selecionado.'
    }    
}
#==============================================================================================================================
preambulo = {

    'funcao':{
        'html': '''
            <p style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">{0}</p> ''',
        'txt_dgp': '''A DECANA DE GESTÃO DE PESSOAS DA UNIVERSIDADE DE BRASÍLIA, 
                    no uso de suas atribuições legais, conferidas pelo Ato da Reitoria nº .72,
                    publicado no DOU n. 13, de 20 de janeiro de 2021, seção 2, página 24,
                    e de acordo com a competência que lhe foi delegada por meio do Ato da Reitoria n. 304,
                    de 23 de março de 2017, publicado no DOU n. 58, de 24 de março de 2017 
                    e à vista do constante no Processo Eletrônico nº {0},''',
        'txt_dgp_substituto': '''A DECANA DE GESTÃO DE PESSOAS EM EXERCÍCIO DA UNIVERSIDADE DE BRASÍLIA, no uso de suas atribuições legais,
                    conferidas pelo ato da Reitoria nº 514, publicado no Diário Oficial da União nº 81, de 28 de abril de 2017, seção 2,
                    página 31 e de acordo com a competência que lhe foi delegada por meio do Ato nº 1593, de 03 de abril de 2017,
                    publicado dia 05 de abril de 2017, no DOU, Seção 1, página 13, e à vista do constante no Processo Eletrônico nº {0}''',
        'txt_dgp_dap': '''O DIRETOR DE ADMINISTRAÇÃO DE PESSOAS DO DECANATO DE GESTÃO DE PESSOAS DA UNIVERSIDADE DE BRASÍLIA,
                       no uso de suas atribuições legais e de acordo com a competência que lhe foi delegada
                       por meio do Ato do Decanato de Gestão de Pessoas n. 1.593, de 03 de abril de 2017,
                       publicado no DOU n. 66, de 05 de abril de 2017 e à vista do constante no Processo Eletrônico nº {0},''',
        'txt_dgp_dap_susbstituto': '''O(A) DIRETOR(A) DE ADMINISTRAÇÃO DE PESSOAS SUSTITUTO(A) DO DECANATO DE GESTÃO DE PESSOAS DA UNIVERSIDADE DE BRASÍLIA,
                       no uso de suas atribuições legais e de acordo com a competência que lhe foi delegada
                       por meio do Ato do Decanato de Gestão de Pessoas n. 1.593, de 03 de abril de 2017,
                       publicado no DOU n. 66, de 05 de abril de 2017 e à vista do constante no Processo Eletrônico nº {0},''',               
        'txt_reitoria': 'A REITORA DA UNIVERSIDADE DE BRASÍLIA, no uso de suas atribuições e considerando o constante no Processo nº {0},',
        'txt_reitoria_substituto': 'O VICE-REITOR, NO EXERCÍCIO DA REITORIA DA UNIVERSIDADE DE BRASÍLIA, no uso de suas atribuições estatutárias e considerando o constante no Processo nº {0}',
        'txt_erro': 'ERRO: Nenhum Tipo de Setor Responsável selecionado.'
    }    
}

preambulo_word = {     

    'funcao':{
        'txt_dgp': '''A DECANA DE GESTÃO DE PESSOAS DA UNIVERSIDADE DE BRASÍLIA, no uso de suas atribuições legais, conferidas pelo Ato da Reitoria nº .72, publicado no DOU n. 13, de 20 de janeiro de 2021, seção 2, página 24, e de acordo com a competência que lhe foi delegada por meio do Ato da Reitoria n. 304, de 23 de março de 2017, publicado no DOU n. 58, de 24 de março de 2017, RESOLVE:''',
        'txt_dgp_substituto': '''A DECANA DE GESTÃO DE PESSOAS EM EXERCÍCIO DA UNIVERSIDADE DE BRASÍLIA, no uso de suas atribuições legais, conferidas pelo ato da Reitoria nº 514, publicado no Diário Oficial da União nº 81, de 28 de abril de 2017, seção 2, página 31 e de acordo com a competência que lhe foi delegada por meio do Ato nº 1593, de 03 de abril de 2017, publicado dia 05 de abril de 2017, no DOU, Seção 1, página 13, RESOLVE:''',
        'txt_dgp_dap': '''O DIRETOR DE ADMINISTRAÇÃO DE PESSOAS DO DECANATO DE GESTÃO DE PESSOAS DA UNIVERSIDADE DE BRASÍLIA, no uso de suas atribuições legais e de acordo com a competência que lhe foi delegada por meio do Ato do Decanato de Gestão de Pessoas n. 1.593, de 03 de abril de 2017, publicado no DOU n. 66, de 05 de abril de 2017, RESOLVE:''',
        'txt_dgp_dap_susbstituto': '''O(A) DIRETOR(A) DE ADMINISTRAÇÃO DE PESSOAS SUSTITUTO(A) DO DECANATO DE GESTÃO DE PESSOAS DA UNIVERSIDADE DE BRASÍLIA, no uso de suas atribuições legais e de acordo com a competência que lhe foi delegada por meio do Ato do Decanato de Gestão de Pessoas n. 1.593, de 03 de abril de 2017, publicado no DOU n. 66, de 05 de abril de 2017, RESOLVE:''',               
        'txt_reitoria': 'A REITORA DA UNIVERSIDADE DE BRASÍLIA, no uso de suas atribuições, RESOLVE:',
        'txt_reitoria_substituto': 'O VICE-REITOR, NO EXERCÍCIO DA REITORIA DA UNIVERSIDADE DE BRASÍLIA, no uso de suas atribuições estatutárias, RESOLVE:',
        'txt_erro': 'ERRO: Nenhum Tipo de Setor Responsável selecionado.'
    }    
}
#==============================================================================================================================
texto_ato = {

        'funcao': {
            'html': '''
                 <p style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">{0}</p> ''',
                'txt_cds': {    
                    'nomeacao': '''Nomear, com mandato de 4 (quatro) anos, {0} {1} para exercer a função de {2} ({3}){4}''', 
                    'exoneracao': 'Exonerar {0} {1} da função de {2} ({3}){4}',
                    'substituicao':'Nomear {0} {1} para substituir {2} ({3}) durante o período de {4}, de {5} a {6}, {7}.', 
                    'substituicao_vago':'Nomear {0} {1} para substituir {2} ({3}) {4}, de {5} a {6}.',
                    'reconducao':'''Reconduzir, a partir de {0}, {1} {2} para exercer a função de {3} ({4}), com mandato de 4 (quatro) anos.'''
                },
                'txt_fgs': {
                    'designacao': 'Designar {0} {1} para exercer a função de {2} ({3}).',
                    'dispensa': 'Dispensar {0} {1} da função de {2} ({3}).',
                    'substituicao': '''Designar {0} {1} para substituir {2} ({3}) durante o período de {4}, de {5} a {6}, {7}.''',
                    'substituicao_vago': '''Designar {0} {1} para substituir {2} ({3}) {4}, de {5} a {6}.'''
                },
                'txt_fccs': {         
                    'designacao': 'Designar, para mandato de 2 (dois) anos, {0} {1} para exercer a função de {2} (FCC).',
                    'dispensa': 'Dispensar, por término de mandato, {0} {1} da função de {2} (FCC).',
                    'substituicao': '''Designar {0} {1} para substituir {2} (FCC), durante o período de {3}, de {4} a {5}, {6}.''',
                    'substituicao_vago': '''Designar {0} {1} para substituir {2} (FCC) {3}, de {4} a {5}.''',
                    'nao_remunerada': {
                        'designacao':'''
                                Art. 1º  Designar {0} {1} para exercer a função não remunerada de {2}.
<p style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">Art. 2º  Este Ato entra em vigor na data de sua publicação no Boletim de Atos Oficiais da UnB (BAO).</p>''', 
                        'dispensa': '''
                                Art. 1º  Dispensar {0} {1} da função não remunerada de {2}.
<p style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">Art. 2º  Este Ato entra em vigor na data de sua publicação no Boletim de Atos Oficiais da UnB (BAO).</p>'''
                    }
                },
                'txt_erro': 'ERRO: Nenhum Tipo de ato selecionado.'
        }
}
#==============================================================================================================================
dirigentes = {
              'html':'<p style="font-size:12pt;font-family:Calibri;text-align:center;word-wrap:normal;margin:6pt;">{0}</p>',
              'dgp':
              {'decanato': 
               {'titular': "Maria do Socorro Mendes Gomes<br>Decana de Gestão de Pessoas", 
                'em_exercicio': "Sheila Perla Maria de Andrade da Silva<br>Decana de Gestão de Pessoas em exercício"
                },
                'dap': 
                {'titular':'Willian Aparecido Rodrigues Soares<br>Diretor de Administração de Pessoas',
                 'em_exercicio': 'nome do substituto<br>Diretor de Administração de Pessoas em exercício'
                 }
              },
              'reitoria':
              {
                'titular': 'Prof ª Márcia Abrahão Moura<br>Reitora',
                'em_exercicio': 'Prof. Enrique Huelva Unternbäumen<br>Vice-Reitor, no exercício da Reitoria'
              }

}
#==============================================================================================================================


