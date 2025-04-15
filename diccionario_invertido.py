def diccionario_invertido(diccionario: dict[str, str]) -> dict[str, str]:
    return {valor: clave for clave, valor in diccionario.items()}
entrada = { 
    "azul": "color",
    "gato": "animal",
    "verde": "color"
    
}

salida = diccionario_invertido(entrada)
print(salida)   
