# Requisitos:
# Ativas
# SC

import pandas as pd

nEstab = '9'

cNames = ('CNPJ_BASICO', 'CNPJ_ORDEM', 'CNPJ_DV', 'IDENTIFICADOR_MATRIZ_FILIAL', 'NOME_FANTASIA', 'SITUACAO_CADASTRAL', 'DATA_SITUACAO_CADASTRAL', 'MOTIVO_SITUACAO_CADASTRAL', 'NOME_CIDADE_EXTERIOR', 'PAIS', 'DATA_INICIO_ATIVIDADE', 'CNAE_FISCAL_PRINCIPAL', 'CNAE_FISCAL_SECUNDARIA', 'TIPO_LOGRADOURO', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'CEP', 'UF', 'MUNICIPIO', 'DDD_1', 'TELEFONE_1', 'DDD_2', 'TELEFONE_2', 'DDD_FAX', 'FAX', 'CORREIO_ELETRONICO', 'SITUACAO_ESPECIAL', 'DATA_SITUACAOO_ESPECIAL')

uCols = ('NOME_FANTASIA', 'SITUACAO_CADASTRAL', 'DATA_INICIO_ATIVIDADE', 'CNAE_FISCAL_PRINCIPAL', 'CNAE_FISCAL_SECUNDARIA', 'UF', 'MUNICIPIO')

df = pd.read_csv('arquivos-brutos/Estabelecimentos' + nEstab + '/estabelecimentos' + nEstab + '.csv', sep=';', names=cNames, usecols=uCols, encoding='ISO-8859-1')

df = df[(df.UF == 'SC') & (df.SITUACAO_CADASTRAL == 2)]

df.to_csv('arquivos-brutos/Estabelecimentos' + nEstab + '/estabelecimentos' + nEstab + '-sc-ativos.csv')

print(df.head())
print(df.shape)
