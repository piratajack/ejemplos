def calcular_total_ventas(lista_ventas):   #Aquí se está definiendo una función llamada calcular_total_ventas.
    resultado = {}     #aca creamos un diccionario que alamcenara el valor por cada producto 
    for producto, cantidad, precio_unitario in lista_ventas:      #aca recorremos cada lista de lista_ventas  
        if producto in resultado:    #Si el producto ya está en el diccionario Se suma a su total actual lo recaudado en esta nueva venta
            resultado[producto] += cantidad * precio_unitario  
        else:              #Si el producto no está en el diccionario se agrega con el valor de la venta actual 
            resultado[producto] = cantidad * precio_unitario
    return resultado   #aca de devolemos el resultado con el valor total de cada producto 
ventas = [     #estas seria nuestras variables de ejemplo 
    ("manzana", 3, 0.5),
    ("banana", 2, 0.75),
    ("manzana", 4, 0.5),
    ("naranja", 5, 0.6)
]

print(calcular_total_ventas(ventas))   #aca imprimimos el valor total de ventas de cada producto 
