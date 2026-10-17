import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_por_volumen,
    descuento_cumulativo,
    descuento_apilado
)

def test_aplicar_descuento_valido():
    precio, porcentaje = 100, 15
    resultado = aplicar_descuento(precio, porcentaje)
    assert resultado == 85.0

def test_aplicar_descuento_precio_negativo_lanza_error():
    precio, porcentaje = -50, 10

    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        aplicar_descuento(precio, porcentaje)

# --- ( BUG 1) ---
def test_calcular_precio_final_con_impuesto_y_descuento():
    # Precio base: $100 | Descuento: 10% -> $90 | Impuesto: 19% de $90 -> $17.1 | Precio final esperado: $107.1
    precio, impuesto, descuento = 100, 19, 10
    resultado = calcular_precio_final(precio, impuesto, descuento)
    assert resultado == 107.1

def test_descuento_por_volumen_mas_de_100_unidades():
    cantidad, precio_unitario = 100, 10  # Subtotal = 1000, Descuento = 20% -> 800
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    assert resultado == 800.0

# --- (BUG 2) ---
def test_descuento_apilado_excede_100_porcentaje():
    precio = 100
    descuentos = [60, 50]  # Suma 110% -> Debe tope en 100% (precio final = 0.0)
    resultado = descuento_apilado(precio, descuentos)
    assert resultado == 0.0

