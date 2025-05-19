# 📊 Superstore Sales Analysis

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seu-usuario/covid19-brasil-analysis/blob/main/notebooks/covid19_analysis.ipynb)

Análise de vendas e lucratividade para uma loja fictícia, focada em gerar insights estratégicos que ajudam na tomada de decisão em marketing, estoque e precificação.

## 🎯 Objetivo
Identificar padrões de vendas, margem de lucro e comportamento de clientes a partir do dataset Superstore, com o intuito de:

- Analisar tendências de vendas ao longo do tempo;

- Avaliar a rentabilidade por produto e categoria;

- Compreender o perfil e comportamento dos clientes;

- Detectar oportunidades para otimizar ações comerciais;

- Apoiar decisões operacionais baseadas em dados.


## 🔍 O que foi feito
- 📥 Leitura e limpeza do dataset Superstore.csv:
   - Remoção de colunas irrelevantes: Country, Postal Code, Row ID
   - Eliminação de duplicatas
   
- 🧹 Tratamento e preparação dos dados:
  - Padronização e organização para análise exploratória

📊 Análise exploratória focada nas principais dimensões do negócio

📈 Visualizações comparativas entre métricas-chave

💡 Geração de insights práticos e acionáveis

## 📈 Principais Insights

| Dimensão       | Insight                                                        |
| -------------- | --------------------------------------------------------------|
| **Categoria**  | `Technology` lidera em lucro e ticket médio; `Furniture` com baixa margem. |
| **Subcategoria**| `Tables` geram prejuízo; `Phones` e `Chairs` se destacam.     |
| **Região**     | Sul tem maior ticket médio, Centro com desempenho fraco.       |
| **Segmento**   | `Corporate` com ticket médio alto; `Consumer` em volume.       |
| **Clientes**   | Top 20 clientes concentram grande parte do lucro.              |
| **Correlação** | Descontos altos reduzem lucro; vendas e lucro moderadamente correlacionados. |

📖 Veja a análise completa em [`ANALYSIS.md`](./ANALYSIS.md)

## 🧠 Conclusões Gerais
- 📦 Volume de vendas nem sempre representa lucratividade.

- ⚠️ Subcategorias deficitárias indicam necessidade de revisão estratégica.

- 👥 O mix de clientes e descontos impacta diretamente a rentabilidade.

- 🌍 Existe potencial para explorar regiões e segmentos subutilizados.

## 🔗 Fonte dos Dados

[Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download)

## 📁 Estrutura

```plaintext
superstore-analysis/
├── data/             # Dataset original
├── notebooks/        # Análise e visualizações (notebooks Jupyter)
├── scripts/          # Scripts auxiliares (limpeza, processamento, gráficos)
├── reports/          # Gráficos exportados e imagens
├── ANALYSIS.md       # Análise detalhada com insights e interpretações
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação principal do projeto
```


## 🛠️ Principais Bibliotecas
#### - Python (pandas, numpy)

#### - Jupyter Notebook

#### - Matplotlib & Seaborn para visualização

#### - Google Colab para execução na nuvem

## 👨‍💻 Sobre o Autor
#### Pedro Augusto Alves Brandão
Aspirante a Cientista de Dados, apaixonado por transformar dados em decisões estratégicas.

## 📘 Acesse o notebook
👉 [Analise Vendas](https://colab.research.google.com/drive/1E2C-8DHi0uzHHOPbs9dFmlH41_x6LwQH?usp=sharing)

## 📄 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [`LICENSE`](./LICENSE) para mais detalhes.

## 🔜 Próximos Passos
- [ ] Previsão de demanda por categoria via regressão
- [ ] Análise estatística mais robusta (média, desvio, outliers)
- [ ] Versão em inglês do projeto
- [ ] Gráficos interativos (Plotly, Tableau Public)
- [ ] Mais análises/comparações

## 💻 Como Executar
Clone este repositório:
````
git clone https://github.com/PedroAABR/covid19-brasil-analysis.git
````
Instale as dependências (recomenda-se uso do Google Colab):

- pandas

- matplotlib

- seaborn

- numpy

Execute o notebook principal no Colab para reproduzir as análises.
