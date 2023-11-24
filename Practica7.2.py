import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Cargar el conjunto de datos desde un archivo CSV
df = pd.read_csv('datos_limpios_premier_league_odds.csv')

# Mapea las etiquetas (1, X, 2) a colores
label_colors = {'1': 'blue', 'X': 'red', '2': 'green'}

# Dividir el conjunto de datos en características (X) y etiquetas (y)
X = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']]
y = df['Resultado']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)  # Puedes ajustar el número de vecinos (k) según tus necesidades

# Ajustar el modelo a los datos de entrenamiento
knn.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = knn.predict(X_test)

# Calcular la precisión del modelo
accuracy = knn.score(X_test, y_test)
print(f"Precisión del modelo KNN: {accuracy * 100:.2f}%")

# Crear una gráfica de dispersión de las características y las predicciones
plt.figure(figsize=(10, 6))
plt.scatter(X_test['ProbabilidadGanaLocal (1)'], X_test['ProbabilidadGanaVisitante (2)'], c=[label_colors[label] for label in y_pred], cmap='viridis')
plt.title('Gráfica de Dispersión de las Características y Predicciones')
plt.xlabel('Probabilidad GanaLocal (1)')
plt.ylabel('ProbabilidadGanaVisitante (2)')
plt.colorbar(label='Predicciones')
plt.show()