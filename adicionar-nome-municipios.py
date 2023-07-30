import pandas as pd

cNames = ('COD_MUNICIPIO', 'DESCRICAO_MUNICIPIO')
dfMunicipios = pd.read_csv('arquivos-brutos/Municipios/municipios.csv', names=cNames, sep=';')

df = pd.read_csv('arquivos-brutos/estabelecimentos-sc.csv')

df2 = df.merge(dfMunicipios, on='COD_MUNICIPIO')
df2.to_csv('arquivos-brutos/estabelecimentos-sc-municipios.csv')
