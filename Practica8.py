import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Cargar el conjunto de datos desde un archivo CSV
df = pd.read_csv('datos_limpios_premier_league_odds.csv')

# Seleccionar las características para el clustering (por ejemplo, las probabilidades y los goles)
X = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']]

# Determinar el número de clústeres (k) - Puedes ajustar esto según tus necesidades
num_clusters = 3

# Crear el modelo K-Means
kmeans = KMeans(n_clusters=num_clusters, random_state=0)

# Ajustar el modelo a las características
kmeans.fit(X)

# Agregar las etiquetas de clúster al conjunto de datos
df['Cluster'] = kmeans.labels_

# Visualizar los resultados
# En este ejemplo, estamos visualizando los clústeres utilizando las dos primeras características (ProbabilidadGanaLocal (1) y ProbabilidadEmpate (X))
plt.scatter(X['ProbabilidadGanaLocal (1)'], X['ProbabilidadEmpate (X)'], c=df['Cluster'], cmap='rainbow')
plt.xlabel('Probabilidad GanaLocal (1)')
plt.ylabel('Probabilidad Empate (X)')
plt.title('Agrupación con K-Means')
plt.show()