import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Cargar tu conjunto de datos desde el archivo CSV
df = pd.read_csv('datos_limpios_premier_league_odds.csv')

# Concatenar las columnas de texto
text = ' '.join(df['EquipoLocal'] + ' ' + df['EquipoVisitante'])

# Crear la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Mostrar la nube de palabras utilizando matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
