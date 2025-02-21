WITH ventana AS (
SELECT 
    d.nombre_departamento,
    SUM(e.salario) OVER (PARTITION BY e.id_departamento ORDER BY e.fecha_contratacion DESC) AS Salario_acumulado
FROM empleados AS e
INNER JOIN departamentos AS d ON
    d.id_departamento=e.id_departamento
)
SELECT nombre_departamento, max(Salario_acumulado)
FROM ventana
GROUP BY nombre_departamento;