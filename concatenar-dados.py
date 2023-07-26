filenames = []

for i in range(10):
    filename = (f'arquivos-brutos/Estabelecimentos{i}/estabelecimentos{i}-sc-ativos.csv')
    filenames.append(filename)

cabecalho = 'COD,NOME_FANTASIA,SITUACAO_CADASTRAL,DATA_INICIO_ATIVIDADE,CNAE_FISCAL_PRINCIPAL,CNAE_FISCAL_SECUNDARIA,UF,MUNICIPIO\n'

with open('arquivos-brutos/estabelecimentos-sc.csv', 'w') as outfile:
    outfile.write(cabecalho) #Escreve o cabeçalho apenas uma vez
    for fname in filenames:
        with open(fname, 'r') as infile:
            next(infile) #Pula o cabeçalho
            for line in infile:
                outfile.write(line)