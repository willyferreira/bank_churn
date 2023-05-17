import pandas as pd

df_original = pd.read_csv(
    filepath_or_buffer='churn.csv'
)

df_original.head()