def valor_total_inventario(inventario: dict[str, tuple[int, float]]) -> float:      #  aca definimos la funcion valor_total_inventario que nos indica que 
                                                                                    #  las claves son cadenas tipo str y los valores son tuplas tipo int y float  
                                                                                    # aca siendo el primer numero entero y el segundo decimal 
                                                                                                    
    total = 0    #aca creamos una variable total con valor a cero 
    for producto, (cantidad, precio) in inventario.items():    #aca con el bucle for recorremos cada par con el diccionario 
        total += cantidad * precio   #aca multiplicamos la cantidad por el precio 
    return total   #aca se devuelve el total del inventario 
inventario = {     #estos serian nuestros productos con sus respectivas cantidades y precios 
    'manzanas': (100, 0.5),
    'naranjas': (100, 0.75),
    'plátanos': (100, 0.6)
}

valor_total = valor_total_inventario(inventario)
print(f"Valor total del inventario: ${valor_total:.2f}")    #aca llamamos la funcion inventario y guardamos en valor total y imprimos el valor 
                                                            #usando f y 2f que nos permite incluir varibles dentro de una cadena de manera clara y directa 
                                                            #osea que el valor solo imprima solo dos decimales y el valor total 