def diccionario_invertido(diccionario: dict[str, str]) -> dict[str, str]:  #Esta línea define una función llamada diccionario_invertido. 
                                                                            #diccionario (diccionario: dict[str, str]) indicandi que los valosres clave seran cadenas de carateres
                                                                            #dict[str, str]: eston indica que tambien nos devueve un diccionario con cadenas de caracteres 
    return {valor: clave for clave, valor in diccionario.items()}    #esta linea usa comprensión de diccionario para invertir las claves y valores.con el bucle for recorremos 
                                                                     #cada par y creamos un nuevo diccionario donde la clave será el valor original, y el valor será la clave original.

entrada = { 
    "azul": "color",
    "gato": "animal",
    "verde": "color"
    
}

salida = diccionario_invertido(entrada) #Llamamos a la funcion en entrada y guardamos en salida 
print(salida)   #con print imprimimos el diccionario invertido 
