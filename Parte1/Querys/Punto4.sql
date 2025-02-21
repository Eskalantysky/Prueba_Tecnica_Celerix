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