import pandas as pd

ti = pd.read_csv(
    r'C:\Users\Julia Telles\Documents\GitHub\cursos_ti_2024.csv',
    sep=';',
    encoding='utf-8-sig'
)


# 1. matrículas

#quantas mulheres estão matriculadas em cursos de ti
mat_fem = ti["QT_MAT_FEM"].sum()
print(f'Mulheres matriculadas: {mat_fem}')

#quantos homens estão matriculados
mat_masc = ti["QT_MAT_MASC"].sum()
print(f'Homens matriculados: {mat_masc}')

#percentual feminino
percentual_mat = (mat_fem / (mat_fem + mat_masc)) * 100
print(f'Percentual de mulheres matriculadas em relação ao total de matriculados: {percentual_mat}')

# 2. número de ingressantes

#quantas mulheres ingressam
ing_fem = ti["QT_ING_FEM"].sum()
print(f'Mulheres ingressantes: {ing_fem}')

#quantos homens ingressam
ing_masc = ti["QT_ING_MASC"].sum()
print(f'Homens ingressantes: {ing_masc}')

#percentual feminino de ingressantes 
percentual_ing = (ing_fem / (ing_fem + ing_masc)) * 100
print(f'Percentual feminino de ingressantes em relação ao total de ingressantes: {percentual_ing}')

# 3. números de concluintes

#quantas mulheres concluem
conc_fem = ti["QT_CONC_FEM"].sum()
print(f'Número de mulheres concluintes: {conc_fem}')

#taxa de conclusão feminina
conc_fem = ti["QT_CONC_FEM"].sum()
conc_masc = ti["QT_CONC_MASC"].sum()

participacao_concluintes = (
    conc_fem /
    (conc_fem + conc_masc)
) * 100
print(f'Taxa de concluintes feminina: {participacao_concluintes}')

# 4. cursos com mais mulheres e cursos com menos mulheres

#cursos com mais mulheres
curso = (
    ti.groupby("NO_CURSO")
      [["QT_MAT_FEM", "QT_MAT"]]
      .sum()
)

curso["PERC_FEM"] = (
    curso["QT_MAT_FEM"] /
    curso["QT_MAT"]
) * 100

print(
    curso.sort_values(
        "PERC_FEM",
        ascending=False
    )
)

# 5. Analise regional
regiao = (
    ti.groupby("NO_REGIAO")
      [["QT_MAT_FEM", "QT_MAT"]]
      .sum()
)

regiao["PERC_FEM"] = (
    regiao["QT_MAT_FEM"] /
    regiao["QT_MAT"]
) * 100

print(f'Matriculadas por região:{regiao}')

# estados com maior participação feminina
estado = (
    ti.groupby("SG_UF")
      [["QT_MAT_FEM", "QT_MAT"]]
      .sum()
)

estado["PERC_FEM"] = (
    estado["QT_MAT_FEM"] /
    estado["QT_MAT"]
) * 100

print(
    estado.sort_values(
        "PERC_FEM",
        ascending=False
    )
)

colunas_sql = [
    'NO_REGIAO',
    'SG_UF',
    'NO_CURSO',
    'QT_ING_FEM',
    'QT_ING_MASC',
    'QT_MAT_FEM',
    'QT_MAT_MASC',
    'QT_CONC_FEM',
    'QT_CONC_MASC'
]

ti_sql = ti[colunas_sql]
print(ti_sql.head())

print(
    ti[
        [
            'NO_REGIAO',
            'SG_UF',
            'NO_CURSO',
            'QT_ING_FEM',
            'QT_ING_MASC',
            'QT_MAT_FEM',
            'QT_MAT_MASC',
            'QT_CONC_FEM',
            'QT_CONC_MASC'
        ]
    ].head()
)

ti_sql = ti[colunas_sql].copy()

ti_sql = ti_sql.dropna(subset=["NO_REGIAO", "SG_UF"])

ti_sql = ti_sql[
    (ti_sql["QT_MAT_FEM"] + ti_sql["QT_MAT_MASC"]) > 0
]

ti_sql.to_csv(
    r'C:\Users\Julia Telles\Documents\GitHub\cursos_ti_sql.csv',
    sep=';',
    index=False,
    encoding='utf-8-sig'
)

print('Arquivo salvo!')