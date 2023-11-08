import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Cargar tu conjunto de datos desde el archivo CSV
df = pd.read_csv('datos_limpios_premier_league_odds.csv')  

# Calcular el promedio de las probabilidades de ganar local (1) para cada equipo
promedio_probabilidad_local = df.groupby('EquipoVisitante')['ProbabilidadGanaVisitante (2)'].mean()

# Obtener el promedio de goles locales para cada equipo
promedio_goles_locales = df.groupby('EquipoVisitante')['GolesVisita'].mean()

# Regresión lineal
X_local = promedio_probabilidad_local
Y_local = promedio_goles_locales

X_local = sm.add_constant(X_local)  # Agregar intercepto

modelo_local = sm.OLS(Y_local, X_local).fit()

print("Regresión lineal para Promedio de Probabilidades Gana Local vs. Promedio de Goles Locales:")
print(modelo_local.summary())

# Gráfico para Promedio de Goles Locales vs. Promedio de Probabilidades de Ganar Local
plt.figure(figsize=(10, 6))
plt.scatter(X_local['ProbabilidadGanaVisitante (2)'], Y_local, label='Promedio de Probabilidades vs. Promedio de Goles Locales')
plt.plot(X_local['ProbabilidadGanaVisitante (2)'], modelo_local.predict(X_local), color='red', label='Recta de Regresión (Promedio de Goles Locales)')
plt.xlabel('Promedio de Probabilidades de Ganar Visitante (1)')
plt.ylabel('Promedio de Goles Visitantes')
plt.title('Regresión Lineal: Promedio de Probabilidades vs. Promedio de Goles Visitantes')
plt.legend()
plt.tight_layout()
plt.show()
