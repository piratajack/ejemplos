def valor_total_inventario(inventario: dict[str, tuple[int, float]]) -> float:
    total = 0
    for producto, (cantidad, precio) in inventario.items():
        total += cantidad * precio
    return total
inventario = {
    'manzanas': (100, 0.5),
    'naranjas': (80, 0.75),
    'plátanos': (50, 0.6)
}

valor_total = valor_total_inventario(inventario)
print(f"Valor total del inventario: ${valor_total:.2f}")
