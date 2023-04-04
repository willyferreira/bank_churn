#1. Instalação e importação de pacotes
import pandas as pd
import numpy as np
import matplotlib.pyplot
import plotly.express as px
import plotly.graph_objects as go

#2.Leitura do dataframe
pd.read_csv(filepath_or_buffer = 'churn.csv', encoding = 'UTF-8')