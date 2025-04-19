def clasificar_estudiantes(lista_estudiantes):     #definimos la funcion clasificar_estudiantes que recibe una lista d eestudiantes 
    clasificacion = {   #creamos un diccionario con tres claves alto,medio,bajo 
        "alto": [],
        "medio": [],
        "bajo": []
    }

    for nombre, calificacion in lista_estudiantes:         #recorremos cada tupla, cada tupla se compone en nombre y clasificasion 
        if calificacion >= 90:                             #Si la nota es 90 o más, se agrega el nombre a la lista "alto"
            clasificacion["alto"].append(nombre)
        elif 70 <= calificacion <= 89:       #             Si está entre 70 y 89, va a "medio"
            clasificacion["medio"].append(nombre)
        else:                                              #Si es menor que 70, va a "bajo"
            clasificacion["bajo"].append(nombre)
    
    return clasificacion                         #devolvemos el reultado con los nombres clasificados 
 

estudiantes = [("Ana", 95), ("Luis", 82), ("Carlos", 68), ("María", 91), ("Jorge", 73), ("Lucía", 55)]     #creamos una lista de tuplas donde cada tupla contiene el nombre y el valor de cada estudiante 

print(clasificar_estudiantes(estudiantes))     #imprimimos en pantalla 
