import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos desde el archivo CSV
df = pd.read_csv('datos_limpios_premier_league_odds.csv')

def Conteo_resultados(df):
    etiquetas = ['GanaLocal', 'GanaVisita', 'Empate']

    # Cálculos y gráficas de ejemplo
    media_goles_locales = df['GolesLocal'].mean()
    moda_resultados = df['Resultado'].mode()[0]

    # Gráfico de barras de resultados
    resultados_counts = df['Resultado'].value_counts()
    resultados_counts.plot(kind='bar')
    plt.title('Frecuencia de Resultados')
    plt.xlabel('Resultado')
    plt.ylabel('Frecuencia')
    plt.xticks(range(len(etiquetas)), etiquetas, rotation= 45) 
    plt.show()

def HistogramaProbayGoles (df):
    #histograma de probabilidades de ganar local (1)
    plt.figure(figsize=(10, 6))
    plt.hist(df['ProbabilidadGanaLocal (1)'], bins=20, color='blue', alpha=0.7)
    plt.title('Distribución de Probabilidades de Ganar Local (1)')
    plt.xlabel('Probabilidad')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show() 
    
    ## Crear histograma de goles locales
    plt.figure(figsize=(10, 6))
    plt.hist(df['GolesLocal'], bins=15, color='green', alpha=0.7)
    plt.title('Distribución de Goles Locales')
    plt.xlabel('Goles')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

    #histograma de probabilidades de ganar visita (2s)
    plt.figure(figsize=(10, 6))
    plt.hist(df['ProbabilidadGanaVisitante (2)'], bins=20, color='orange', alpha=0.7)
    plt.title('Distribución de Probabilidades de Ganar Visitante (2)')
    plt.xlabel('Probabilidad')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

    #Crear histograma de goles visitantes
    plt.figure(figsize=(10, 6))
    plt.hist(df['GolesVisita'], bins=15, color='purple', alpha=0.7)
    plt.title('Distribución de Goles de Visitantes')
    plt.xlabel('Goles')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

def GraficasFecha(df):
    fechas = pd.to_datetime(df['Fecha'])
    plt.figure(figsize=(12, 6))
    probabilidad_local = df['ProbabilidadGanaLocal (1)']
    probabilidad_empate = df['ProbabilidadEmpate (X)']
    probabilidad_visitante = df['ProbabilidadGanaVisitante (2)']

    plt.fill_between(fechas, probabilidad_local, label='Gana Local (1)', color='blue', alpha=0.5)
    plt.fill_between(fechas, probabilidad_empate, label='Empate (X)', color='red', alpha=0.5)
    plt.fill_between(fechas, probabilidad_visitante, label='Gana Visitante (2)', color='green', alpha=0.5)

    plt.title('Probabilidades a lo largo del tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()
    
Conteo_resultados(df)
HistogramaProbayGoles(df)
GraficasFecha(df)