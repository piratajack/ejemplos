
def calcular_salario_total_por_departamento(departamentos):
    total_por_departamento = {}
    for nombre_departamento, empleados in departamentos.items():
        total = sum(empleados.values())
        total_por_departamento[nombre_departamento] = total
    return total_por_departamento
datos = {
    "Ventas": {"Ana": 3000, "Luis": 2500},
    "Marketing": {"Clara": 4000, "Pedro": 3500},
    "IT": {"Jorge": 5000, "Marta": 4800}
}

resultado = calcular_salario_total_por_departamento(datos)
print(resultado)
