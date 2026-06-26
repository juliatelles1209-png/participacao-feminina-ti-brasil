select * from cursos_ti;

SELECT * FROM cursos_ti LIMIT 10;

SELECT DISTINCT
    c.sg_uf,
    r.id_regiao
FROM cursos_ti c
JOIN regiao r
ON c.no_regiao = r.nome_regiao

WHERE c.sg_uf IS NOT NULL;

SELECT * FROM estado;

SELECT DISTINCT no_curso

FROM cursos_ti

WHERE no_curso IS NOT NULL;

SELECT * FROM curso;


SELECT

    e.id_estado,

    cu.id_curso,

    c.qt_ing_fem,

    c.qt_ing_masc,

    c.qt_mat_fem,

    c.qt_mat_masc,

    c.qt_conc_fem,

    c.qt_conc_masc

FROM cursos_ti c

JOIN estado e

ON c.sg_uf = e.sg_uf

JOIN curso cu

ON c.no_curso = cu.nome_curso

WHERE c.sg_uf IS NOT NULL;

SELECT COUNT(*) FROM indicadores;

SELECT

    cu.nome_curso,

    e.sg_uf,

    i.qt_mat_fem,

    i.qt_mat_masc

FROM indicadores i

JOIN curso cu

ON i.id_curso = cu.id_curso

JOIN estado e

ON i.id_estado = e.id_estado

LIMIT 20;

SELECT

    e.sg_uf,

    ROUND(

        SUM(i.qt_mat_fem) * 100.0 /

        SUM(i.qt_mat_fem + i.qt_mat_masc),

        2

    ) AS percentual

FROM indicadores i

JOIN estado e

ON i.id_estado = e.id_estado

GROUP BY e.sg_uf

ORDER BY percentual DESC;