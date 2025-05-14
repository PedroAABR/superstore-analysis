# 📊 Superstore Sales Analysis

Análise de vendas e lucratividade para uma loja fictícia, focada em gerar insights estratégicos que ajudam na tomada de decisão em marketing, estoque e precificação.

## 🎯 Objetivo

Identificar padrões de vendas, margem de lucro e comportamento de clientes a partir do dataset Superstore. Resultados orientam ações comerciais e operacionais.


## 🔍 O que foi feito
Leitura e limpeza do dataset Superstore.csv.

Remoção de colunas irrelevantes: Country, Postal Code, Row ID.

Eliminação de duplicatas.

Análise exploratória com foco nas principais dimensões do negócio.

Visualizações comparativas entre métricas chave.

Geração de insights práticos e acionáveis.

## 📈 Principais Insights

| Dimensão       | Insight                                                        |
| -------------- | --------------------------------------------------------------|
| **Categoria**  | `Technology` lidera em lucro e ticket médio; `Furniture` com baixa margem. |
| **Subcategoria**| `Tables` geram prejuízo; `Phones` e `Chairs` se destacam.     |
| **Região**     | Sul tem maior ticket médio, Centro com desempenho fraco.       |
| **Segmento**   | `Corporate` com ticket médio alto; `Consumer` em volume.       |
| **Clientes**   | Top 20 clientes concentram grande parte do lucro.              |
| **Correlação** | Descontos altos reduzem lucro; vendas e lucro moderadamente correlacionados. |

Para análises detalhadas, veja: [Análise Completa](./ANALYSIS.md)

## 🧠 Conclusões Gerais
#### Volume de vendas nem sempre representa lucratividade.

#### Subcategorias deficitárias indicam necessidade de revisão estratégica.

#### O mix de clientes e descontos impacta diretamente a rentabilidade.

#### Existe potencial para explorar regiões e segmentos subutilizados.


## 🔗 Fonte dos Dados

Dataset fictício utilizado:
[Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download)

## 📁 Estrutura

superstore-analysis/
├── data/          # Dataset original
├── notebooks/     # Análise e visualizações (notebooks Jupyter)
├── scripts/       # Scripts auxiliares (limpeza, processamento, gráficos)
├── reports/       # Gráficos exportados e imagens
├── ANALYSIS.md    # Análise detalhada com insights e interpretações
├── requirements.txt  # Dependências do projeto
└── README.md      # Documentação principal do projeto


## 🛠️ Principais Bibliotecas
- Python (pandas, numpy)
- Jupyter Notebook
- Matplotlib e Seaborn para visualização

## Sobre o autor
Pedro Augusto Alves Brandão — Data Analyst aspirante, apaixonado por transformar dados em decisões estratégicas.

## 📘 Acesse o notebook
👉 [Analise Vendas](https://colab.research.google.com/drive/1E2C-8DHi0uzHHOPbs9dFmlH41_x6LwQH?usp=sharing)

## 📄 Licença
Projeto para uso educacional.

## 🔜 Próximos Passos
- Previsão de demanda por categoria via regressão
- Análise estatística mais robusta (média, desvio, outliers)
- Versão em inglês do projeto
- Gráficos interativos (Plotly, Tableau Public)

## 🚀 Como Executar

```bash
git clone https://github.com/PedroAABR/superstore-analysis.git
cd superstore-analysis
pip install -r requirements.txt
jupyter notebook
