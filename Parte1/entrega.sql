INSERT INTO empleados VALUES
(6, 'Elena', 'López', '2023-05-01', 33000.00, 3);

UPDATE empleados
SET salario=37000.00
WHERE id_empleado=2;

CREATE TRIGGER actualizar_stock
AFTER INSERT ON detalle_pedidos
FOR EACH ROW
BEGIN
    UPDATE productos
    SET stock = stock - NEW.cantidad
    WHERE id_producto = NEW.id_producto;
END;

SELECT 
    p.nombre_producto,
    p.stock,
    count(dp.id_pedido)                 AS veces_pedido, 
    sum(dp.cantidad)                    AS unidades_vendidas, 
    max(ped.fecha_pedido)               AS fecha_ultimo_pedido,
    sum(dp.cantidad*dp.precio_unitario) AS ingresos_totales
FROM 
    detalle_pedidos AS dp
INNER JOIN 
    pedidos AS ped ON
        dp.id_pedido=ped.id_pedido
INNER JOIN 
    productos AS p ON
        dp.id_producto=p.id_producto
GROUP BY 
    p.nombre_producto, 
    p.stock
HAVING count(dp.cantidad)>1;

CREATE INDEX idx_pedidos_id_cliente ON pedidos(id_cliente);
CREATE INDEX idx_pedidos_fecha_pedido ON pedidos(fecha_pedido);
CREATE INDEX idx_pedidos_total ON pedidos(total);

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