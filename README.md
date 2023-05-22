# Churn Rate - Clientes de Banco

## Objetivo do projeto
O projeto visa a criação de modelo preditivo capaz de identificar o perfil de clientes propensos a cancelar um serviço/produto em um determinado período de tempo, ação que eleva o "churn rate", métrica utilizada pelas empresas para mensurar a taxa de abandono de sua base, o que impacta diretamente o faturamento.

### Dados utilizados na análise e na criação do modelo
Para criação do modelo foi utilizado o dataset disponibilizado na plataforma Kaggle, acessível [por esse link](https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers).
## Estágio atual do projeto
Atualmente, o projeto está na fase de Análise Exploratória de dados.
São utilizadas nesse estágio as bibliotecas Numpy e Pandas para manipulação e transformação dos dados, além da biblioteca Seaborn para geração dos gráficos.

### Checklist do projeto

- [ ] Análise Exploratória de dados
  - [x] Análise univariada
  - [x] Análise bivariada
  - [x] Análise multivariada e correlação
- [ ] Divisão e seleção de features (treino e teste)
- [ ] Aplicação dos modelos
- [ ] Resultados estatísticos
- [ ] Descrição de importância das features

________________________________________________________________


**Matriz de correlação:**

```
#Criação dos subplots
fig, axs = plt.subplots(ncols = 1, nrows = 2, sharex=True, height_ratios=[0.8, 0.2])
#Título da imagem
plt.suptitle('Distribuição do Score de Crédito')
#Gráfico 1 - Histograma
sns.histplot(x = df.ScoreCredito, kde = True, ax = axs[0], stat = 'count', cumulative = False)
#Gráfico 2 - Boxplot
sns.boxplot(x = df.ScoreCredito, fliersize = 2, notch = True, ax = axs[1])
```

![Distribuição do Score de Crédito](https://github.com/willyferreira/bank_churn/blob/7a95da430e6baa0e5f75cf92eb67688175aeda5f/figures/EDA_ScoreCredito.png)


