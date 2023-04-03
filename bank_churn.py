import pandas as pd

df = pd.read_csv(
    filepath_or_buffer='churn.csv'
)

df.head()

df.rename(
    columns={
        'CustomerId': 'Id_Cliente',
        'Surname': 'Sobrenome', 
        'CreditScore': 'Score',
        'Geography': 'Nacionalidade',
        'Gender': 'Genero',
        'Age': 'Idade',
        'Tenure': 'Tempo_Relacionamento',
        'Balance': 'Saldo',
        'NumOfProducts': 'Qtd_Produtos',
        'HasCrCard': 'Tem_CartaoCred',
        'IsActiveMember': 'Ativo',
        'EstimatedSalary': 'Salario_Estimado',
        'Exited': 'ExCliente'
        },
    inplace = True
)

df.head()

df.drop(
    columns={
        'RowNumber'
    },
    inplace=True
)