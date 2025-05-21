import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações gerais de visualização
sns.set(style="whitegrid")
#plt.style.use("seaborn")
plt.style.use("ggplot")  # Usa um estilo válido do Matplotlib

# Carregar dados
data = pd.read_csv('data/dataset.csv')

# Visão geral dos dados
print("Primeiras linhas do dataset:")
print(data.head())

print("\nInformações sobre o dataset:")
print(data.info())

print("\nEstatísticas descritivas do dataset:")
print(data.describe())

# Limpeza de Dados (exemplo)
# Remover valores ausentes
data = data.dropna()

# Análise Exploratória de Dados (EDA)
# Histograma de uma coluna específica (exemplo)
plt.figure(figsize=(10, 6))
sns.histplot(data['coluna_interesse'], kde=True)
plt.title('Distribuição da Coluna de Interesse')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()

# Gráfico de dispersão entre duas colunas (exemplo)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='coluna_x', y='coluna_y', data=data)
plt.title('Relação entre Coluna X e Coluna Y')
plt.xlabel('Coluna X')
plt.ylabel('Coluna Y')
plt.show()

# Matriz de correlação
plt.figure(figsize=(12, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlação')
plt.show()

# Geração de Relatórios (sumário)
def gerar_relatorio(data):
    with open('data/report.txt', 'w') as file:
        file.write("Relatório de Análise de Dados\n")
        file.write("="*40 + "\n\n")
        
        file.write("Informações Gerais:\n")
        file.write(data.info(buf=None) + "\n\n")
        
        file.write("Estatísticas Descritivas:\n")
        file.write(data.describe().to_string() + "\n\n")
        
        file.write("Matriz de Correlação:\n")
        file.write(correlation_matrix.to_string() + "\n")

gerar_relatorio(data)

print("Análise completa. O relatório foi gerado em 'data/report.txt'.")
