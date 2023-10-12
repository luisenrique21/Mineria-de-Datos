import pandas as pd
from scipy import stats

# Cargar el conjunto de datos desde el archivo CSV
df = pd.read_csv('datos_limpios_premier_league_odds.csv')

# Realizar ANOVA para comparar probabilidades y goles en función de 'Resultado'
resultado_1 = df[df['Resultado'] == '1']['ProbabilidadGanaLocal (1)']
resultado_x = df[df['Resultado'] == 'X']['ProbabilidadEmpate (X)']
resultado_2 = df[df['Resultado'] == '2']['ProbabilidadGanaVisitante (2)']

# Realizar el ANOVA para las probabilidades
f_statistic_prob, p_value_prob = stats.f_oneway(resultado_1, resultado_x, resultado_2)

# Realizar el ANOVA para los goles locales
goles_local = df['GolesLocal']
f_statistic_goles_local, p_value_goles_local = stats.f_oneway(goles_local, resultado_1, resultado_x, resultado_2)

# Realizar el ANOVA para los goles de visita
goles_visita = df['GolesVisita']
f_statistic_goles_visita, p_value_goles_visita = stats.f_oneway(goles_visita, resultado_1, resultado_x, resultado_2)

# Imprimir los resultados
print("ANOVA para Probabilidades:")
print(f"Estadística F: {f_statistic_prob}")
print(f"Valor P: {p_value_prob}")

print("\nANOVA para Goles Locales:")
print(f"Estadística F: {f_statistic_goles_local}")
print(f"Valor P: {p_value_goles_local}")

print("\nANOVA para Goles de Visita:")
print(f"Estadística F: {f_statistic_goles_visita}")
print(f"Valor P: {p_value_goles_visita}")

# Comprobar si los resultados son significativos
alpha = 0.05

if p_value_prob < alpha:
    print("\nDiferencias significativas encontradas en las probabilidades.")
else:
    print("\nNo se encontraron diferencias significativas en las probabilidades.")

if p_value_goles_local < alpha:
    print("Diferencias significativas encontradas en los goles locales.")
else:
    print("No se encontraron diferencias significativas en los goles locales.")

if p_value_goles_visita < alpha:
    print("Diferencias significativas encontradas en los goles de visita.")
else:
    print("No se encontraron diferencias significativas en los goles de visita.")
