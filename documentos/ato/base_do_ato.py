from documentos.ato.partes_do_ato import *
from auxiliares.funcoes import *
from auxiliares.connection import *



def gerar_ato(formulario):
    # recebendo partes do Ato
    _epigarafe_ = epigrafe_ato(formulario)
    _ementa_ = ementa_ato(formulario)
    _preambulo_ = preambulo_ato(formulario)
    _texto_ato_ = texto_do_ato(formulario)
    _assinatura_ = assinatura_ato(formulario)
    _nome_arquivo_ = f"Ato_{formulario['nome_servidor']}.html"
    # escrevendo partes no arquivo
    with open(_nome_arquivo_, "w", encoding='utf-8') as f:
        f.write('''
        <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
        <html lang="pt-br" >
        <head>
        <!--
        <meta http-equiv="Pragma" content="no-cache" />
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">-->
        <style type="text/css">
        p.Citacao {font-size:10pt;font-family:Calibri;word-wrap:normal;margin:4pt 0 4pt 160px;text-align:justify;} p.Fonte_10 {font-size:10pt;} p.Item_Alinea_Letra {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt 6pt 6pt 120px;counter-increment:letra_minuscula;} p.Item_Alinea_Letra:before {content:counter(letra_minuscula, lower-latin) ") ";display:inline-block;width:5mm;font-weight:normal;} p.Item_Inciso_Romano {font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0mm;margin:6pt 6pt 6pt 120px;counter-increment:romano_maiusculo;counter-reset:letra_minuscula;} p.Item_Inciso_Romano:before {content:counter(romano_maiusculo, upper-roman) " - ";display:inline-block;width:15mm;font-weight:normal;} p.Item_Nivel1 {text-transform:uppercase;font-weight:bold;background-color:#e6e6e6;font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;counter-increment:item-n1;counter-reset:item-n2 item-n3 item-n4 romano_maiusculo letra_minuscula;} p.Item_Nivel1:before {content:counter(item-n1) ".";display:inline-block;width:25mm;font-weight:normal;} p.Item_Nivel2 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:item-n2;counter-reset:item-n3 item-n4 romano_maiusculo letra_minuscula;} p.Item_Nivel2:before {content:counter(item-n1) "." counter(item-n2) ".";display:inline-block;width:25mm;font-weight:normal;} p.Item_Nivel3 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:item-n3;counter-reset:item-n4 romano_maiusculo letra_minuscula;} p.Item_Nivel3:before {content:counter(item-n1) "." counter(item-n2) "." counter(item-n3) ".";display:inline-block;width:25mm;font-weight:normal;} p.Item_Nivel4 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:item-n4;counter-reset:romano_maiusculo letra_minuscula;} p.Item_Nivel4:before {content:counter(item-n1) "." counter(item-n2) "." counter(item-n3) "."  counter(item-n4) ".";display:inline-block;width:25mm;font-weight:normal;} p.Paragrafo_Numerado_Nivel1 {font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0mm;margin:6pt;counter-increment:paragrafo-n1;counter-reset:paragrafo-n2 paragrafo-n3 paragrafo-n4 romano_maiusculo letra_minuscula;} p.Paragrafo_Numerado_Nivel1:before {content:counter(paragrafo-n1) ".";display:inline-block;width:25mm;font-weight:normal;} p.Paragrafo_Numerado_Nivel2 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:paragrafo-n2;counter-reset:paragrafo-n3 paragrafo-n4 romano_maiusculo letra_minuscula;} p.Paragrafo_Numerado_Nivel2:before {content:counter(paragrafo-n1) "." counter(paragrafo-n2) ".";display:inline-block;width:25mm;font-weight:normal;} p.Paragrafo_Numerado_Nivel3 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:paragrafo-n3;counter-reset:paragrafo-n4 romano_maiusculo letra_minuscula;} p.Paragrafo_Numerado_Nivel3:before {content:counter(paragrafo-n1) "." counter(paragrafo-n2) "." counter(paragrafo-n3) ".";display:inline-block;width:25mm;font-weight:normal;} p.Paragrafo_Numerado_Nivel4 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:paragrafo-n4;counter-reset:romano_maiusculo letra_minuscula;} p.Paragrafo_Numerado_Nivel4:before {content:counter(paragrafo-n1) "." counter(paragrafo-n2) "." counter(paragrafo-n3) "." counter(paragrafo-n4) ".";display:inline-block;width:25mm;font-weight:normal;} p.Tabela_texto_6 {font-size:6pt;font-family:Calibri;text-align:left;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_8 {font-size:8pt;font-family:Calibri;text-align:left;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_8_Alinhado_Direita_UnB {font-size:8pt;font-family:Calibri;text-align:rigth;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_8_Centralizado_UnB {font-size:8pt;font-family:Calibri;text-align:center;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_Alinhado_Direita {font-size:11pt;font-family:Calibri;text-align:right;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_Alinhado_Esquerda {font-size:11pt;font-family:Calibri;text-align:left;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_Centralizado {font-size:11pt;font-family:Calibri;text-align:center;word-wrap:normal;margin:0 3pt 0;} p.Tachado {font-size:11pt;font-family:Calibri;text-indent:1.18in;text-align:justify;word-wrap:normal;text-decoration:line-through;} p.Teste_UnB {font-size:12pt;} p.Texto_Alinhado_Direita {font-size:12pt;font-family:Calibri;text-align:right;word-wrap:normal;margin:6pt;} p.Texto_Alinhado_Esquerda {font-size:12pt;font-family:Calibri;text-align:left;word-wrap:normal;margin:6pt;} p.Texto_Alinhado_Esquerda_Espacamento_Simples {font-size:12pt;font-family:Calibri;text-align:left;word-wrap:normal;margin:0;} p.Texto_Alinhado_Esquerda_Espacamento_Simples_Maiusc {font-size:12pt;font-family:Calibri;text-align:left;text-transform:uppercase;word-wrap:normal;margin:0;} p.Texto_Centralizado {font-size:12pt;font-family:Calibri;text-align:center;word-wrap:normal;margin:6pt;} p.Texto_Centralizado_Maiusculas {font-size:13pt;font-family:Calibri;text-align:center;text-transform:uppercase;word-wrap:normal;} p.Texto_Centralizado_Maiusculas_Negrito {font-weight:bold;font-size:13pt;font-family:Calibri;text-align:center;text-transform:uppercase;word-wrap:normal;} p.Texto_Espaco_Duplo_Recuo_Primeira_Linha {letter-spacing:0.2em;font-weight:bold;font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;} p.Texto_Fundo_Cinza_Maiusculas_Negrito {text-transform:uppercase;font-weight:bold;background-color:#e6e6e6;font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;} p.Texto_Fundo_Cinza_Negrito {font-weight:bold;background-color:#e6e6e6;font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;} p.Texto_Justificado {font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;} p.Texto_Justificado_Maiusculas {font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;text-transform:uppercase;} p.Texto_Justificado_Recuo_Primeira_Linha {font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;} p.Texto_Mono_Espacado {font-size:8pt;font-family:Calibri;text-align:left;white-space:pre;word-wrap:normal;margin:2pt;} 
        </style>''')
        f.write(f'''
        <title>{formulario['documento_selecionado']}</title>
        </head>
        <body>
            {_epigarafe_}
            {_ementa_}
            {_preambulo_}
        <p class="Texto_Alinhado_Esquerda_Espacamento_Simples">&nbsp;</p>
        <p>&nbsp;</p>
        <p style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">R E S O L V E:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>
        <p>&nbsp;</p>
            {_texto_ato_}
        <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>
        <p>&nbsp;</p>
            {_assinatura_}
        <br>
        <br>
        <br>
        <div style="font-size: 11px;">
        <hr>
        <b>Referência:</b> Processo nº <span>{formulario['numero_do_sei']}</span>
        <hr>
        </div>
        </html>''')
    # grando texto do ato no banco de dados    
    dados_publicacao = gerar_conteudo_publicacao(formulario['numero_ato'], formulario['ano_do_ato'], _texto_ato_)

    # botão para baixar o formulário
    baixar_documento(_nome_arquivo_)

    # criando bando de dados, tabela e inserção
    conectar = criar_conexao('atosgerados_db')
    inserir_atos(conectar, 'atos_publicacao', dados_publicacao)

    
    
    
    




        
        