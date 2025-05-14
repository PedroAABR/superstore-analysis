# 📊 Superstore Sales Analysis

Análise exploratória completa com foco em identificar padrões de vendas, lucratividade e comportamento de clientes em uma loja fictícia. A partir dos dados do Superstore Dataset, foram gerados insights estratégicos por categoria, subcategoria, região, segmento e perfil de cliente.

### 📊 Exemplo de Análise

<img src="reports/MapaCalor_correlações.png" alt="Correlações" width="400"/>
<img src="reports/Quantidade_categoria.png" alt="Quantidade de Vendas Categoria" width="400"/>

## 🎯 Objetivo

Compreender os principais fatores que impactam as vendas e a rentabilidade da operação, analisando diferentes dimensões como tipo de produto, região, perfil do consumidor e descontos. Os resultados podem orientar ações de marketing, precificação, fidelização e gestão de estoque.


## 🔍 O que foi feito
Leitura e limpeza do dataset Superstore.csv.

Remoção de colunas irrelevantes: Country, Postal Code, Row ID.

Eliminação de duplicatas.

Análise exploratória com foco nas principais dimensões do negócio.

Visualizações comparativas entre métricas chave.

Geração de insights práticos e acionáveis.

## 📁 Análises realizadas, Resultados e Insights

As análises completas por dimensão (categoria, região, cliente, etc.), resultados das análises mais aprofundados e insights mais precisos foram movidas para um arquivo separado para melhor organização.

👉 Confira aqui: [🔍 Análise Detalhada](./ANALYSIS.md)

## 📈 Resultados e Insights

| Dimensão         | Insight                                                                          |
| ---------------- | -------------------------------------------------------------------------------- |
| **Categoria**    | `Technology` lidera em lucro e ticket médio; `Furniture` tem margem baixa.       |
| **Subcategoria** | `Tables` apresentaram prejuízo; `Phones` e `Chairs` se destacam positivamente.   |
| **Região**       | Sul tem maior ticket médio, mas menor volume. Centro tem desempenho fraco.       |
| **Segmento**     | `Corporate` tem melhor ticket médio; `Consumer` lidera em volume.                |
| **Clientes**     | Top 20 concentram boa parte da receita — ideais para estratégias de fidelização. |
| **Correlação**   | Descontos altos reduzem o lucro; vendas e lucro possuem correlação moderada.     |

## 🧠 Conclusões Gerais
#### Volume de vendas nem sempre representa lucratividade.

#### Subcategorias deficitárias indicam necessidade de revisão estratégica.

#### O mix de clientes e descontos impacta diretamente a rentabilidade.

#### Existe potencial para explorar regiões e segmentos subutilizados.


## 🔗 Fonte dos Dados

[Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download)

### Obs: Os dados são fictícios e os insights são apenas para uso educacional.

## 📁 Estrutura

superstore-analysis/
│
├── data/          # Dataset original
├── notebooks/     # Análise e visualizações
├── scripts/       # Scripts auxiliares (limpeza, gráficos)
├── reports/       # Gráficos exportados e imagens
└── requirements.txt


## 🛠️ Principais Bibliotecas
- pandas  
- matplotlib  
- seaborn  
- numpy  
- jupyter


## ▶️ Como executar

### Clone o repositório
git clone https://github.com/seu-usuario/superstore-analysis.git
cd superstore-analysis

### Instale as dependências
pip install -r requirements.txt

### Execute a análise
jupyter notebook

## 📘 Acesse o notebook
👉 [Analise_Vendas](https://colab.research.google.com/drive/1E2C-8DHi0uzHHOPbs9dFmlH41_x6LwQH?usp=sharing)

## 📌 Próximos passos: 
Incluir previsão de demanda por categoria com regressão.

Criar uma análise estatística (média, desvio, outliers) ou uso de boxplots poderia enriquecer.

Criar uma versão em inglês do projeto.

Criar um gráfico interativo (Plotly ou Tableau Public embutido).
