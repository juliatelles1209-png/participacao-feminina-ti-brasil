INSERT INTO regiao (nome_regiao)
SELECT DISTINCT no_regiao
FROM cursos_ti
WHERE no_regiao IS NOT NULL;
SELECT * FROM regiao;

INSERT INTO estado (sg_uf, id_regiao)
SELECT * FROM estado;


INSERT INTO curso (nome_curso)
SELECT * FROM curso;


INSERT INTO indicadores (

    id_estado,

    id_curso,

    qt_ing_fem,

    qt_ing_masc,

    qt_mat_fem,

    qt_mat_masc,

    qt_conc_fem,

    qt_conc_masc

)
SELECT * FROM indicadores;