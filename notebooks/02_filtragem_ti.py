import pandas as pd

df = pd.read_csv(
    r'C:\Users\Julia Telles\Downloads\microdados_censo_da_educacao_superior_2024\microdados_censo_da_educacao_superior_2024\dados\MICRODADOS_CADASTRO_CURSOS_2024.CSV',
    sep=';',
    encoding='latin1',
    low_memory=False
)

cursos_ti = [
    'ANÁLISE E DESENVOLVIMENTO DE SISTEMAS',
    'BANCO DE DADOS',
    'CIÊNCIA DA COMPUTAÇÃO',
    'CIÊNCIAS DA COMPUTAÇÃO',
    'CIÊNCIAS DE COMPUTAÇÃO',
    'COMPUTAÇÃO',
    'COMPUTAÇÃO E INFORMÁTICA',
    'COMPUTAÇÃO EM NUVEM',
    'DESENVOLVIMENTO DE SISTEMAS',
    'DESENVOLVIMENTO DE SOFTWARE MULTIPLATAFORMA',
    'ENGENHARIA DA COMPUTAÇÃO',
    'ENGENHARIA DE COMPUTAÇÃO',
    'ENGENHARIA DE COMPUTAÇÃO E INFORMAÇÃO',
    'ENGENHARIA DE SOFTWARE',
    'GESTÃO DA TECNOLOGIA DA INFORMAÇÃO',
    'INTELIGÊNCIA ARTIFICIAL: SISTEMAS DE DADOS INTELIGENTES',
    'INTERNET DAS COISAS E COMPUTAÇÃO EM NUVEM',
    'REDES DE COMPUTADORES',
    'SEGURANÇA DA INFORMAÇÃO',
    'SEGURANÇA DA INFORMAÇÃO E DEFESA CIBERNÉTICA',
    'SISTEMAS DE COMPUTAÇÃO',
    'SISTEMAS DE INFORMAÇÃO',
    'SISTEMAS PARA INTERNET',
    'TECNOLOGIA DA INFORMAÇÃO',
    'TECNOLOGIA DA INFORMAÇÃO PARA NEGÓCIOS DIGITAIS',
    'TECNOLOGIA EM DESENVOLVIMENTO DE SOFTWARE MULTIPLATAFORMA'
]
padrao = '|'.join(cursos_ti)

ti = df[
    df['NO_CURSO'].str.contains(
        padrao,
        case=False,
        na=False
    )
]

print(
    ti[
        [
            'NO_REGIAO',
            'SG_UF',
            'NO_CURSO',
            'QT_MAT_FEM',
            'QT_MAT_MASC'
        ]
    ].head(20)
)

print(ti['NO_CURSO'].value_counts())

cursos = pd.DataFrame(
    sorted(ti['NO_CURSO'].unique()),
    columns=['NO_CURSO']
)

print(ti.shape)

print(
    ti[
        [
            'NO_REGIAO',
            'SG_UF',
            'NO_CURSO',
            'QT_MAT_FEM'
        ]
    ].head()
)

ti.to_csv(
    r'C:\Users\Julia Telles\Documents\GitHub\cursos_ti_2024.csv',
    sep=';',
    encoding='utf-8-sig',
    index=False
)
