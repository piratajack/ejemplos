
def calcular_salario_total_por_departamento(departamentos):  #aca definimos la funcion que toma como diccionario el parametro llamado departamento 
    total_por_departamento = {}  #creamos un diccionario basio para guardar el salario total 
    for nombre_departamento, empleados in departamentos.items():   #este for recorre cada departamento y sus empleados 
        total = sum(empleados.values())  #devuelve todos los salarios de los empleados del departamento 
        total_por_departamento[nombre_departamento] = total  #aca se guardan el total de salarios de ese departamento en el diccionario 
    return total_por_departamento   #alfinal s devuelven el diccionario con el total por departamento 
datos = {   #estos son los datos que se van a ingresar en el diccionario 
    "Ventas": {"Ana": 3000, "Luis": 2500},
    "Marketing": {"Clara": 4000, "Pedro": 3500},  
    "IT": {"Jorge": 5000, "Marta": 4800}
}

resultado = calcular_salario_total_por_departamento(datos)  #aca nos imprime en pantalla el resultado de la funcion 
print(resultado)
