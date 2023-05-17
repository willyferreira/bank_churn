# Análise de churn - Clientes de Banco 
## Dataset
O dataset utilizado para as análises contidas nesse repositório está disponível [nesse link](https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers)
### Estágio atual das análises
Atualmente realizo a análise exploratória dos dados, gerando gráficos das variáveis utilizando o pacote Seaborn.

*Exemplos de análises feitas:*
`git status`


````#Criação dos subplots
fig, axs = plt.subplots(ncols = 1, nrows = 2, sharex=True, height_ratios=[0.8, 0.2])
#Título da imagem
plt.suptitle('Distribuição do Score de Crédito')
#Gráfico 1 - Histograma
sns.histplot(x = df.ScoreCredito, kde = True, ax = axs[0], stat = 'count', cumulative = False)
#Gráfico 2 - Boxplot
sns.boxplot(x = df.ScoreCredito, fliersize = 2, notch = True, ax = axs[1])
````

### Objetivo
Após as análises exploratórias, o objetivo é a criação de modelos preditivos que possam explicar a variável-alvo (Churn). O Churn é uma métrica importante para uma empresa, pois dá aos gestores a noção de quantos clientes cancelaram um serviço ou deixaram de consumir um produto em um determinado período de tempo.


