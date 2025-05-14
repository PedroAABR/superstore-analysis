# Remover colunas desnecessárias
df.drop(['Country','Postal Code', 'Row ID'], axis=1, inplace=True)

# Verificar e remover duplicatas
df.drop_duplicates(inplace=True)
