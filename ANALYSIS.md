# 📊 Análise Detalhada - Superstore Sales Analysis

Este documento apresenta uma visão aprofundada das análises realizadas por dimensão no dataset Superstore.

---

## 📚 Sumário

- [🔹 Categoria](#categoria)
- [🔹 Sub-Categoria](#sub-categoria)
- [🔹 Região](#região)
- [🔹 Segmento](#segmento)
- [🔹 Cliente (Top 20)](#cliente-top-20)
- [🔹 Correlação entre variáveis](#correlação-entre-variáveis)
- [📈 Resultados e Insights](#resultados-e-insights)

---

# 🔹 Categoria

# 📊 Total de Vendas por Categoria

<img src="reports/Vendas_categoria.png"/>

## 🔍 O que foi feito

Foi criado um gráfico de barras para apresentar o **total de vendas (em valor monetário)** de uma loja fictícia, segmentado por categoria de produtos. Os dados foram agrupados pela variável:

- `Category`: categoria do produto (`Furniture`, `Office Supplies`, `Technology`)
- `Sales`: valor monetário das vendas

A soma total por categoria foi calculada e visualizada com `seaborn.barplot()`.

## 📈 Principais Insights

1. **Categoria com maior faturamento: Technology**
   - A categoria **Technology** lidera as vendas, com um total superior a **$840.000**, indicando alto valor agregado por item ou forte volume de vendas.

2. **Furniture e Office Supplies em patamares similares**
   - Ambas as categorias apresentam vendas totais entre **$720.000 e $750.000**, com Furniture levemente à frente.
   - Isso sugere um **desempenho equilibrado** entre os segmentos, mas com potencial de crescimento em estratégias distintas.

3. **Tecnologia como motor de receita**
   - O domínio da categoria Technology pode indicar:
     - Alta demanda por eletrônicos e acessórios
     - Maiores margens por item
     - Campanhas promocionais eficazes nesse segmento

## 🧠 Conclusões Gerais

- A análise por categoria fornece **visão estratégica da composição da receita**, útil para ações de marketing, reposição de estoque e foco em atendimento especializado.
- Sugere-se acompanhar essa análise com:
  - **Lucro por categoria** (e não apenas vendas)
  - **Ticket médio**
  - **Frequência de compra por segmento**

Esse tipo de visualização é fundamental em **dashboards comerciais, relatórios de desempenho e apresentações executivas**.

  <img src="reports/Quantidade_categoria.png" width="300"/>
  <img src="reports/Lucro_categoria.png" width="300"/>


### 🔸 Comparativo visual entre lucro x vendas por categoria
<img src="reports/LucroVendas_categoria.png" width="800"/>

### 🔸 Ticket médio por categoria
<img src="reports/TicketMedio_categoria.png" width="800"/>

---

## 🔹 Sub-Categoria

### 🔸 Total de vendas, quantidade, lucro por sub-categoria
<p align="left">
  <img src="reports/Vendas_subcategoria.png" width="600"/>
  <img src="reports/Quantidade_subcategoria.png" width="600"/>
  <img src="reports/Lucro_subcategoria.png" width="600"/>
</p>

### 🔸 Comparativo lucro x vendas por sub-categoria
<img src="reports/LucroVendas_subcategoria.png" width="800"/>

### 🔸 Ticket médio por sub-categoria
<img src="reports/TicketMedio_subcategoria.png" width="800"/>

---

## 🔹 Região

### 🔸 Total de vendas, quantidade, lucro por região
<p align="left">
  <img src="reports/Vendas_regiao.png" width="300"/>
  <img src="reports/Quantidade_regiao.png" width="300"/>
  <img src="reports/Lucro_regiao.png" width="300"/>
</p>

### 🔸 Comparativo lucro x vendas por região
<img src="reports/LucroVendas_regiao.png" width="400"/>

### 🔸 Ticket médio por região
<img src="reports/TicketMedio_regiao.png" width="400"/>

---

## 🔹 Segmento

### 🔸 Total de vendas, quantidade, lucro por segmento
<p align="left">
  <img src="reports/Vendas_segmento.png" width="300"/>
  <img src="reports/Quantidade_segmento.png" width="300"/>
  <img src="reports/Lucro_segmento.png" width="300"/>
</p>

### 🔸 Comparativo lucro x vendas por segmento
<img src="reports/LucroVendas_segmento.png" width="400"/>

### 🔸 Ticket médio por segmento
<img src="reports/TicketMedio_segmento.png" width="400"/>

---

## 🔹 Cliente (Top 20)

### 🔸 Maior volume de vendas
<img src="reports/Vendas_consumidor.png" width="800"/>

### 🔸 Maior lucro gerado
<img src="reports/Lucro_consumidor.png" width="800"/>

### 🔸 Maior quantidade comprada
<img src="reports/Quantidade_consumidor.png" width="800"/>

---

## 🔹 Correlação entre variáveis

### 🔸 Mapa de calor entre Sales, Quantity, Discount, Profit
<img src="reports/MapaCalor_correlações.png" width="800"/>

---

## 📈 Resultados e Insights

### ✅ Categoria
- *Office Supplies* teve o maior volume de vendas, mas não o maior lucro.
- *Technology* gerou o maior lucro total, indicando alta margem.
- *Furniture* apresenta lucro mais baixo — possível revisão de estratégias.
- Maior ticket médio em *Technology*.

### ✅ Sub-Categoria
- *Chairs* e *Phones* lideram em vendas e lucro.
- *Tables* com prejuízo — alerta de possível problema.
- *Copiers* tem maior ticket médio.
- Estratégias devem variar por subcategoria.

### ✅ Região
- *West* e *East* dominam em vendas.
- *Central* tem lucro fraco — oportunidade de melhoria.
- Maior ticket médio na região *South*.

### ✅ Segmento
- *Consumer* lidera em volume.
- *Corporate* apresenta maior ticket médio.
- *Home Office* tem desempenho inferior — foco potencial para campanhas.

### ✅ Cliente
- Top 20 concentram a maior parte do lucro.
- Volume ≠ Lucro → atenção ao desempenho individual de clientes.

### ✅ Correlação
- Correlação fraca entre Sales e Profit.
- *Discount* afeta negativamente o lucro.
- Volume (Quantity) tem pouco impacto no lucro.

---
## Conclusões e Recomendações

- Volume de vendas não garante lucro.
- Revisar subcategorias deficitárias para melhoria de margem.
- Ajustar estratégias por região e segmento.
- Focar em retenção dos clientes mais lucrativos.
- Reduzir descontos abusivos para proteger rentabilidade.

---

## Referências

- Dataset: [Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

---

## Sobre o Projeto

Este documento complementa o README principal, detalhando a análise exploratória e os insights estratégicos.

---

