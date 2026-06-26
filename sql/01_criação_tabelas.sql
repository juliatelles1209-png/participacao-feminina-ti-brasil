CREATE TABLE cursos_ti (
    no_regiao VARCHAR(50),
    sg_uf VARCHAR(2),
    no_curso VARCHAR(255),

    qt_ing_fem INTEGER,
    qt_ing_masc INTEGER,

    qt_mat_fem INTEGER,
    qt_mat_masc INTEGER,

    qt_conc_fem INTEGER,
    qt_conc_masc INTEGER
);


CREATE TABLE regiao (
    id_regiao SERIAL PRIMARY KEY,
    nome_regiao VARCHAR(30) UNIQUE
);

CREATE TABLE estado (
    id_estado SERIAL PRIMARY KEY,
    sg_uf CHAR(2) UNIQUE,
    id_regiao INTEGER REFERENCES regiao(id_regiao)
);


CREATE TABLE curso (

    id_curso SERIAL PRIMARY KEY,

    nome_curso VARCHAR(150) UNIQUE

);


CREATE TABLE indicadores (

    id_indicador SERIAL PRIMARY KEY,

    id_estado INTEGER REFERENCES estado(id_estado),

    id_curso INTEGER REFERENCES curso(id_curso),

    qt_ing_fem INTEGER,

    qt_ing_masc INTEGER,

    qt_mat_fem INTEGER,

    qt_mat_masc INTEGER,

    qt_conc_fem INTEGER,

    qt_conc_masc INTEGER

);


