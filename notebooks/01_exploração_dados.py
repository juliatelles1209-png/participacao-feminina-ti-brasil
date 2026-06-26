import pandas as pd

df = pd.read_csv(
    r'C:\Users\Julia Telles\Documents\GitHub\Dados\MICRODADOS_CADASTRO_CURSOS_2024.CSV',
    sep=';',
    encoding='latin1',
)

print(df.head())
print(df.columns)
print(df.info())

#valores vazios
print(df.isnull().sum())

#estados existentes
print(df['SG_UF'].value_counts())

#cursos existentes
print(df['NO_CURSO'].nunique())