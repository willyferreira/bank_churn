#1. Instalação e importação de pacotes
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

#2.Leitura do dataframe
df = pd.read_csv(filepath_or_buffer = 'churn.csv', encoding = 'UTF-8')

    #2.1. Manipulação do dataframe
    #Exclusão da coluna RowNumber
    df.drop(columns = {'RowNumber'}, inplace = True) 
    df.head()

    #Alteração do nome das colunas 
    df.rename(columns = {
        'CustomerId': 'Id_Cliente',
        'Surname': 'Nome',
        'CreditScore': 'Score_Credito',
        'Geography': 'Nacionalidade',
        'Gender': 'Genero',
        'Age': 'Idade',
        'Tenure': 'Tempo_Fidelidade',
        'Balance': 'Saldo',
        'NumOfProducts': 'Qtd_Produtos',
        'HasCrCard': 'Tem_Cartao',
        'IsActiveMember': 'Cliente_Ativo',
        'EstimatedSalary': 'Salario_Estimado',
        'Exited': 'Ex_Cliente'},
        inplace = True
        )
    df.head()


