import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# 1. GERANDO DADOS
# Definimos 4 centros específicos (posições X e Y) para evitar números negativos
centros_iniciais = [[10, 50], [80, 20], [30, 80], [100, 100]] 
X_matriz_bruta, _ = make_blobs(n_samples=300, centers=centros_iniciais, cluster_std=8.0, random_state=42)

# 2. ESTRUTURANDO COM PANDAS
# Convertendo a matriz matemática em uma tabela legível com colunas nomeadas
tabela = pd.DataFrame(X_matriz_bruta, columns=['Horas_Jogadas', 'Moedas_de_Ouro'])

# 3. CÉREBRO: O CLASSIFICADOR K-MEANS
kmeans = KMeans(n_clusters=4, init="k-means++", random_state=42)

# O algoritmo analisa os dados, define os grupos e já cria uma coluna nova na tabela com o resultado
tabela['Perfil_Atribuido'] = kmeans.fit_predict(tabela[['Horas_Jogadas', 'Moedas_de_Ouro']])

# Imprime as primeiras 15 linhas no terminal 
print("--- Tabela de Resultados ---")
print(tabela.head(15))
print("\n--------------------------")

# 4. OLHOS: RENDERIZANDO COM MATPLOTLIB
plt.figure(figsize=(9, 6))

# Plota os dados da tabela. A cor (c) é colorida automaticamente usando a coluna 'Perfil_Atribuido'
plt.scatter(
    tabela['Horas_Jogadas'], 
    tabela['Moedas_de_Ouro'], 
    c=tabela['Perfil_Atribuido'], 
    s=40, 
    cmap="viridis", 
    alpha=0.7,
    label="Jogadores"
)

# Destaca os centroides geométricos que o K-Means estabeleceu
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=200,
    c="red",
    marker="X",
    label="Centroides (Média do Grupo)"
)

plt.title("Clusterização de Perfis de Jogadores (K-Means)")
plt.xlabel("Horas Jogadas")
plt.ylabel("Moedas de Ouro")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

# Exibe a interface gráfica
plt.show()