import datetime

lista_de_documentos = ["", "Ato", "Nota Técnica"] # BARRA LATERAL

lista_de_tipos_de_ato = ["","Nomeação de CD", "Exoneração de CD", 
                            "Substituição de CD", "Recondução de CD", 
                            "Designação de FG", "Dispensa de FG", "Substituição de FG", 
                            "Designação de FCC", "Dispensa de FCC", "Substituição de FCC", "FCC não remunerada"] # FORMULÁRIO

lista_de_setores = ["", "DGP", "DGP/DAP", "REITORIA"] # FORMULÁRIO

lista_finalidades_do_ato = ["", "Manutenção de Funções"]

lista_de_nome_funcoes = ["",
                         "Chefe", "Subchefe", "Coordenador", "Coordenadora",
                         "Coordenadora de Pós-graduação", "Coordenador de Pós-graduação",
                         "Coordenadora de Graduação", "Coordenador de Graduação",
                         "Diretora", "Diretor", "Vice-diretora", "Vice-diretor",
                         "Secretária", "Secretário", "Decana", "Decano", "Prefeito", "Prefeita",
                         "Outros (Usar campo 'Descrição da Função')"]

lista_de_nome_funcoes_generos = ["",
                         "o Chefe", "a Chefe", "o Subchefe", "a Subchefe", "o Coordenador", "a Coordenadora",
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

dict_dirigentes_responsaveis = {'dgp':
                                    {'decanato': 
                                        {'titular': "Decano(a) titular", 
                                         'em_exercicio': "Decano(a) em exercício"},
                                     'dap': 
                                        {'titular':"Diretor(a) titular",
                                         'em_exercicio': "Diretor(a) em exercício"}
                                    },
                                    'reitoria':
                                        {
                                        'titular': "Reitor(a)",
                                        'em_exercicio': "Vice-Reitor(a)"
                                        }
                                }

###########################################################################################################################

modelo_ato_em_branco = {"Número SEI do modelo de ato": 9449709}

# capturando ano
data_atual = datetime.date.today()
ano_atual = data_atual.year

lista_meses_ano = {1:'janeiro',
                   2:'fevereiro',
                   3:'março',
                   4:'abril',
                   5:'maio',
                   6:'junho',
                   7:'julho',
                   8:'agosto',
                   9:'setembro',
                   10:'outubro',
                   11:'novembro',
                   12:'dezembro'}

lista_dias_mes = [dia for dia in range(1,32)]
lista_de_anos = [dia for dia in range(2022, (ano_atual + 1))]
