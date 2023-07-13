import datetime

lista_de_documentos = ["", "Ato", "Nota Técnica"] # BARRA LATERAL

lista_de_tipos_de_ato = ["","Nomeação de CD", "Exoneração de CD", 
                            "Substituição de CD", "Recondução de CD", 
                            "Designação de FG", "Dispensa de FG", "Substituição de FG", 
                            "Designação de FCC", "Dispensa de FCC", "Substituição de FCC", "FCC não remunerada"] # FORMULÁRIO

lista_de_setores = ["", "DGP", "DGP/DAP", "REITORIA"] # FORMULÁRIO

lista_finalidades_do_ato = ["", "Manutenção de Funções"]

lista_de_nome_funcoes = ["",
                         "Chefe", "Coordenador", "Coordenadora",
                         "Coordenadora de Pós-graduação", "Coordenador de Pós-graduação",
                         "Coordenadora de Graduação", "Coordenador de Graduação",
                         "Diretora", "Diretor", "Vice-diretora", "Vice-diretor",
                         "Secretária", "Secretário", "Decana", "Decano", "Prefeito", "Prefeita",
                         "Outros (Usar campo 'Descrição da Função')"]

lista_de_nome_funcoes_generos = ["",
                         "o Chefe", "a Chefe", "o Coordenador", "a Coordenadora",
                         "a Coordenadora de Pós-graduação", "o Coordenador de Pós-graduação",
                         "a Coordenadora de Graduação", "o Coordenador de Graduação",
                         "a Diretora", "o Diretor", "a Vice-diretora", "o Vice-diretor",
                         "a Secretária", "o Secretário", "a Decana", "o Decano", "o Prefeito", "a Prefeita",
                         "Outros (Usar campo 'Descrição da Função')"]

lista_de_tipos_funcoes = ["", "FCC", "FUNÇÃO NÃO REMUNERADA", "CD-01", "CD-02", "CD-03", "CD-04", "FG-01", "FG-02", "FG-03"] # FORMULÁRIO

dict_de_tipos_funcoes = {'cds': ["","CD-01", "CD-02", "CD-03", "CD-04"],
                         'fgs': ["","FG-01", "FG-02", "FG-03"],
                         'fccs': ["", "FCC", "FUNÇÃO NÃO REMUNERADA",]}

lista_de_categorias_funcionais = ["", 
                                  "o servidor", "a servidora",
                                  "o docente", "a docente",
                                  "o Professor do Magistério Superior", "a Professora do Magistério Superior",
                                  "Outros (Usar campo 'Nome do Servidor')"]

###########################################################################################################################

# capturando ano
data_atual = datetime.date.today()
ano_atual = data_atual.year

lista_meses_ano = ['janeiro',
                   'fevereiro',
                   'março',
                   'abril',
                   'maio',
                   'junho',
                   'julho',
                   'agosto',
                   'setembro',
                   'outubro',
                   'novembro',
                   'dezembro']

lista_dias_mes = [dia for dia in range(1,32)]
lista_de_anos = [dia for dia in range(2022, (ano_atual + 1))]


#print(dict_de_tipos_funcoes.get('cds')[1])