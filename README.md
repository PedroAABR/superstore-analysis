# 📊 Superstore Sales Analysis

Este projeto realiza uma análise exploratória detalhada dos dados de vendas de uma loja fictícia, com foco em identificar padrões de desempenho por categoria, subcategoria, região, segmento e cliente — destacando produtos mais lucrativos, oportunidades de melhoria e comportamentos que impactam a rentabilidade.

## 🎯 Objetivo

Entender os principais fatores que impactam as vendas e a lucratividade de uma loja fictícia com base nos dados do Superstore. A partir dessa análise, gerar insights acionáveis que poderiam ser aplicados para decisões estratégicas em marketing, precificação, e gestão de categorias de produtos.


## 🔍 O que foi feito
Análise exploratória dos dados do Superstore
Carregamento e limpeza do dataset:

Leitura do arquivo Superstore.csv.

Remoção de colunas irrelevantes: Country, Postal Code, Row ID.

Eliminação de duplicatas.

## 📁 Análises realizadas
### 🔹 Categoria
Total de vendas, quantidade, lucro por categoria.

Comparativo visual entre lucro x vendas.

Cálculo do ticket médio por categoria.

### 🔹 Sub-Categoria
Total de vendas, quantidade, lucro por sub-categoria.

Gráfico com dois eixos: lucro x vendas.

Ticket médio por sub-categoria.

### 🔹 Região
Análise de vendas, quantidade e lucro por região.

Comparação visual de lucro x vendas por região.

Cálculo do ticket médio por região.

### 🔹 Segmento
Análise de vendas, quantidade e lucro por segmento (Consumer, Corporate, Home Office).

Comparativo de lucro x vendas por segmento.

Ticket médio por segmento.

### 🔹 Cliente
Top 20 consumidores com:

Maior volume de vendas.

Maior lucro gerado.

Maior quantidade comprada.

### 🔹 Correlação entre variáveis
Mapa de calor com correlação entre variáveis numéricas como Sales, Quantity, Discount, Profit.

## 📈 Resultados e Insights
### ✅ Categoria
Office Supplies teve a maior quantidade de vendas, mas não necessariamente o maior lucro.

Technology gerou o maior lucro total, mostrando que itens tecnológicos possuem maior margem.

Furniture teve vendas razoáveis, mas lucro mais baixo em comparação — possível foco de revisão de margem.

O ticket médio foi mais alto em Technology, evidenciando compras de maior valor unitário.

### ✅ Sub-Categoria
Subcategorias como Chairs e Phones se destacaram em vendas e lucro.

Algumas subcategorias, como Tables, apresentaram lucro negativo — possível prejuízo.

Copiers teve o maior ticket médio, sugerindo serem itens de alto valor.

Estratégias diferentes podem ser aplicadas a subcategorias com alto volume e baixo lucro.

### ✅ Região
West e East concentram maior volume de vendas.

A região Central teve menor lucro — oportunidade para melhorar performance ou ajustar estratégias.

O ticket médio foi maior no Sul (South), mesmo com menor volume de vendas.

### ✅ Segmento
Segmento Consumer é o que mais compra em volume.

Segmento Corporate apresenta maior ticket médio, o que pode indicar maior potencial de lucro por cliente.

Home Office tem desempenho mais fraco — pode ser explorado com campanhas específicas.

### ✅ Cliente
Top 20 clientes concentram parte significativa do lucro e vendas — potencial para estratégias de retenção e up-sell.

Clientes com grande volume nem sempre são os mais lucrativos — reforça a importância de analisar lucro por cliente.

### ✅ Correlação
Correlação positiva entre Sales e Profit, mas não muito forte.

Discount possui correlação negativa com Profit, sugerindo que grandes descontos prejudicam a rentabilidade.

Quantity tem correlação baixa com lucro, reforçando que volume nem sempre significa ganho.

| Dimensão         | Insight                                                                          |
| ---------------- | -------------------------------------------------------------------------------- |
| **Categoria**    | `Technology` lidera em lucro e ticket médio; `Furniture` tem margem baixa.       |
| **Subcategoria** | `Tables` apresentaram prejuízo; `Phones` e `Chairs` se destacam positivamente.   |
| **Região**       | Sul tem maior ticket médio, mas menor volume. Centro tem desempenho fraco.       |
| **Segmento**     | `Corporate` tem melhor ticket médio; `Consumer` lidera em volume.                |
| **Clientes**     | Top 20 concentram boa parte da receita — ideais para estratégias de fidelização. |
| **Correlação**   | Descontos altos reduzem o lucro; vendas e lucro possuem correlação moderada.     |

## 🧠 Conclusões Gerais
Volume de vendas nem sempre representa lucratividade.

Subcategorias deficitárias indicam necessidade de revisão estratégica.

O mix de clientes e descontos impacta diretamente a rentabilidade.

Existe potencial para explorar regiões e segmentos subutilizados.


## 🔗 Fonte dos Dados

[Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download)

## 📁 Estrutura

superstore-analysis/
│
├── data/          # Dataset original
├── notebooks/     # Análise e visualizações
├── scripts/       # Scripts auxiliares (limpeza, gráficos)
├── reports/       # Gráficos exportados e imagens
└── requirements.txt


## 🛠️ Principais Bibliotecas
pandas

matplotlib

seaborn

numpy

jupyter

## ▶️ Como executar

### Clone o repositório
git clone https://github.com/seu-usuario/superstore-analysis.git
cd superstore-analysis

### Instale as dependências
pip install -r requirements.txt

### Execute a análise
jupyter notebook

## 📘 Acesse o notebook
👉 [Clique aqui para abrir a análise no Jupyter Notebook <!-- ajuste o nome real -->](https://colab.research.google.com/drive/1E2C-8DHi0uzHHOPbs9dFmlH41_x6LwQH?usp=sharing)
