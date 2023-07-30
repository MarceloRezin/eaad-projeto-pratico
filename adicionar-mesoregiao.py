import pandas as pd

dfMesoregioes = pd.read_csv('arquivos-brutos/Municipios/municipios-mesoregiao.csv')

df = pd.read_csv('arquivos-brutos/estabelecimentos-sc-municipios.csv')

df2 = df.merge(dfMesoregioes, left_on='DESCRICAO_MUNICIPIO', right_on='NOME_SEF',)

df2 = df2.drop(columns=['INDEX','COD','COD_MUNICIPIO','DESCRICAO_MUNICIPIO','COD_SEF', 'NOME_SEF'])

df2.to_csv('arquivos-brutos/estabelecimentos-sc-municipios-mesoregiao.csv', index=False)
