import pandas as pd

# Cargar el conjunto de datos desde el archivo CSV
df = pd.read_csv('premier_league_odds.csv')

# 1. Eliminar columnas no deseadas
columnas_a_eliminar = [ 'Round', 'HomeTeamPoints', 'AwayTeamPoints', 'HomeTeamScoredGoals', 'AwayTeamScoredGoals', 'HomeTeamConcededGoals', 'AwayTeamConcededGoals']
df = df.drop(columns=columnas_a_eliminar)

# 2. Renombrar columnas
nuevos_nombres = {
    'Date': 'Fecha',
    'HomeTeam': 'EquipoLocal',
    'AwayTeam': 'EquipoVisitante',
    '1': 'ProbabilidadGanaLocal (1)',
    'X': 'ProbabilidadEmpate (X)',
    '2': 'ProbabilidadGanaVisitante (2)',
    'HomeTeamGoals': 'GolesLocal',
    'AwayTeamGoals': 'GolesVisita', 
    'Result': 'Resultado'
}
df = df.rename(columns=nuevos_nombres)

# 3. Rellenar valores nulos
df['ProbabilidadGanaLocal (1)'] = df['ProbabilidadGanaLocal (1)'].fillna(0)
df['ProbabilidadEmpate (X)'] = df['ProbabilidadEmpate (X)'].fillna(0)
df['ProbabilidadGanaVisitante (2)'] = df['ProbabilidadGanaVisitante (2)'].fillna(0)

# 4. Convertir la columna 'Fecha' a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

resultado_column = df.pop('Resultado')
df['Resultado'] = resultado_column

# 5. Mostrar el DataFrame resultante
df.to_csv('datos_limpios_premier_league_odds.csv', index=False)
