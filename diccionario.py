
def frecuencia_caracteres(cadena: str) -> dict[str, int]:  #aca definimos la funcion de python , str y int nos indica que son valores que espera valores tipo sting y valores enteros 
    frecuencia = {} #aca se crea un diccionario llamado frecuencia que vamos a ir llenado las veces que aparece cada caracter 
    for caracter in cadena: #aca recorro la cadena y tomara un valor de la cadena 
        if caracter in frecuencia:  #aca miramos si el caracter ya esta en el contador 
            frecuencia[caracter] += 1   #si el caracter no esta en el diccionario aumentamos 1 en su contador 
        else:  #si el caracter no esta en el diccionario 
            frecuencia[caracter] = 1 #lo agregamos con 1 por que es la primera vez que lo encontramos 
    return frecuencia     #retorna la frecuencia del resultado final 

texto = "hola mundo" 
texto = "hola mundo" #esta seria nuestra varible que contiene el texto y que podemos asignarle nustro valor 
resultado = frecuencia_caracteres(texto) #aca llamamos a la funcion que queremos llamar 
print(resultado)   #aca imprimo el resultado final 
