# Quantidade total por sub-categoria
subcategory_quantity = df.groupby('Sub-Category')['Quantity'].sum().reset_index()

# Gráfico de barras
plt.figure(figsize=(20,6))
sns.barplot(x='Sub-Category', y='Quantity', data=subcategory_quantity)
plt.title('Quantidade total por Sub-Categoria')
plt.show()

# Total de vendas por sub-categoria
subcategory_sales = df.groupby('Sub-Category')['Sales'].sum().reset_index()

# Gráfico de barras
plt.figure(figsize=(20,6))
sns.barplot(x='Sub-Category', y='Sales', data=subcategory_sales)
plt.title('Total de vendas por Sub-Categoria')
plt.show()

# Gráfico com dois eixos Vendas X Quantidade total por Sub-Categoria
fig, ax1 = plt.subplots(figsize=(20,6))

ax2 = ax1.twinx()
sns.barplot(x='Sub-Category', y='Quantity', data=subcategory_quantity, color='skyblue', ax=ax1)
sns.lineplot(x='Sub-Category', y='Sales', data=subcategory_sales, color='red', marker='o', ax=ax2)

ax1.set_ylabel('Quantidade', color='skyblue')
ax2.set_ylabel('Vendas (Sales)', color='red')
plt.title('Quantidade x Vendas por Sub-Categoria')
ax1.tick_params(axis='x', rotation=45)
plt.show()

# Junta os dois DataFrames pela Sub-Category
df_comparativo = pd.merge(subcategory_quantity, subcategory_sales, on='Sub-Category')

# Calcula o ticket médio por subcategoria
df_comparativo['Ticket Médio'] = df_comparativo['Sales'] / df_comparativo['Quantity']

# Ordenar para melhor visualização (opcional)
df_comparativo = df_comparativo.sort_values(by='Ticket Médio', ascending=False)

# Gráfico
plt.figure(figsize=(20,6))
sns.barplot(x='Sub-Category', y='Ticket Médio', data=df_comparativo, palette='coolwarm')
plt.title('Ticket Médio por Sub-Categoria (Sales / Quantity)')
plt.xticks(rotation=45)
plt.show()

# Lucro por sub-categoria
subcategory_profit = df.groupby('Sub-Category')['Profit'].sum().reset_index()

# Gráfico de barras
plt.figure(figsize=(20,6))
sns.barplot(x='Sub-Category', y='Profit', data=subcategory_profit)
plt.title('Lucro por Sub-Categoria')
plt.show()

# Total de vendas por categoria
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

# Gráfico de barras
plt.figure(figsize=(8,6))
sns.barplot(x='Category', y='Sales', data=category_sales)
plt.title('Total de Vendas por Categoria')
plt.show()

# Total de vendas por região
region_sales = df.groupby('Region')['Sales'].sum().reset_index()

# Gráfico de barras
plt.figure(figsize=(8,6))
sns.barplot(x='Region', y='Sales', data=region_sales)
plt.title('Total de Vendas por Região')
plt.show()

# Lucro por região
region_profit = df.groupby('Region')['Profit'].sum().reset_index()

# Gráfico de barras
plt.figure(figsize=(8,6))
sns.barplot(x='Region', y='Profit', data=region_profit)
plt.title('Lucro por Região')
plt.show()

# Gráfico com dois eixos
fig, ax1 = plt.subplots(figsize=(20,6))

ax2 = ax1.twinx()
sns.barplot(x='Region', y='Profit', data=region_profit, color='skyblue', ax=ax1)
sns.lineplot(x='Region', y='Sales', data=region_sales, color='red', marker='o', ax=ax2)

ax1.set_ylabel('Lucro', color='skyblue')
ax2.set_ylabel('Vendas', color='red')
plt.title('Lucro x Vendas por Região')
ax1.tick_params(axis='x', rotation=45)
plt.show()

# Lucro por segmento
segment_profit = df.groupby('Segment')['Profit'].sum().reset_index()

# Gráfico de barras
plt.figure(figsize=(8,6))
sns.barplot(x ='Segment', y = 'Profit', data=segment_profit)
plt.title('Lucro por segmento')
plt.show()

# Vendas por consumidor
costumer_sales = df.groupby('Customer Name')['Sales'].sum().reset_index()
#Top 20 consumidores
top_20_customers_sales = costumer_sales.sort_values(by='Sales', ascending=False).head(20)

plt.figure(figsize=(12,6))
sns.barplot(x='Customer Name', y='Sales', data=top_20_customers_sales)
plt.title('Top 20 Clientes com Maior Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Lucro por consumidor
costumer_profit = df.groupby('Customer Name')['Profit'].sum().reset_index()
#Top 20 consumidores
top_20_customers_profit = costumer_profit.sort_values(by='Profit', ascending=False).head(20)

plt.figure(figsize=(12,6))
sns.barplot(x='Customer Name', y='Profit', data=top_20_customers_profit)
plt.title('Top 20 Clientes com Maior Lucro')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico com dois eixos
fig, ax1 = plt.subplots(figsize=(20,6))

ax2 = ax1.twinx()
sns.barplot(x='Customer Name', y='Profit', data=top_20_customers_profit, color='skyblue', ax=ax1)
sns.lineplot(x='Customer Name', y='Sales', data=top_20_customers_sales, color='red', marker='o', ax=ax2)

ax1.set_ylabel('Lucro', color='skyblue')
ax2.set_ylabel('Vendas', color='red')
plt.title('Top 20 Lucro x Vendas por Consumidor')
ax1.tick_params(axis='x', rotation=45)
plt.show()


# Seleciona apenas colunas numéricas
numeric_df = df.select_dtypes(include='number')

# Gera o mapa de calor das correlações
plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Mapa de Calor das Correlações')
plt.show()
