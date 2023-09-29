import pandas as pd

df = pd.read_csv('datos_limpios_premier_league_odds.csv')

media = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']].mean()
moda = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']].mode().iloc[0]
conteo = df.shape[0]
minimo = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']].min()
maximo = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']].max()
sumatoria = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']].sum()
varianza = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']].var()
desviacion_estandar = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']].std()
asimetria = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']].skew()
kurtosis = df[['ProbabilidadGanaLocal (1)', 'ProbabilidadEmpate (X)', 'ProbabilidadGanaVisitante (2)', 'GolesLocal', 'GolesVisita']].kurtosis()

# Mostrar los resultados
print("\t\tMedia:")
print(media)
print("\n\t\tModa:")
print(moda)
print("\n\t\tConteo:")
print("Son", conteo, "registros")
print("\n\t\tMínimo:")
print(minimo)
print("\n\t\tMáximo:")
print(maximo)
print("\n\t\tSumatoria:")
print(sumatoria)
print("\n\t\tVarianza:")
print(varianza)
print("\n\tDesviación Estándar:")
print(desviacion_estandar)
print("\n\t\tAsimetría:")
print(asimetria)
print("\n\t\tKurtosis:")
print(kurtosis)
