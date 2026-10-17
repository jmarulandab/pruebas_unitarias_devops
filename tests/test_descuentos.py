import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_por_volumen,
    descuento_cumulativo,
    descuento_apilado
)

# --- Pruebas aplicar_descuento ---
def test_aplicar_descuento_valido():
    # Arrange
    precio, porcentaje = 100, 15
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 85.0

def test_aplicar_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -50, 10
    # Act & Assert
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        aplicar_descuento(precio, porcentaje)

def test_aplicar_descuento_porcentaje_invalido_lanza_error():
    # Arrange
    precio = 100
    # Act & Assert
    with pytest.raises(ValueError, match="El porcentaje debe estar entre 0 y 100"):
        aplicar_descuento(precio, 150)

# --- Pruebas calcular_descuento ---
def test_calcular_descuento_valido():
    # Arrange
    precio, porcentaje = 200, 10
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 20.0

def test_calcular_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -100, 10
    # Act & Assert
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        calcular_descuento(precio, porcentaje)

def test_calcular_descuento_porcentaje_invalido_lanza_error():
    # Arrange
    precio = 100
    # Act & Assert
    with pytest.raises(ValueError, match="El porcentaje debe estar entre 0 y 100"):
        calcular_descuento(precio, -5)

# --- Pruebas calcular_precio_final ---
def test_calcular_precio_final_con_impuesto_y_descuento():
    # Arrange
    precio, impuesto, descuento = 100, 19, 10
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == 107.1

def test_calcular_precio_final_validaciones_errores():
    # Arrange / Act / Assert
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        calcular_precio_final(-100, 19, 10)
    with pytest.raises(ValueError, match="El impuesto no puede ser negativo"):
        calcular_precio_final(100, -19, 10)
    with pytest.raises(ValueError, match="El descuento debe estar entre 0 y 100"):
        calcular_precio_final(100, 19, 110)

# --- Pruebas descuento_por_volumen ---
@pytest.mark.parametrize("cantidad,precio_unitario,esperado", [
    (100, 10, 800.0),   # 20% desc
    (50, 10, 425.0),    # 15% desc
    (20, 10, 180.0),    # 10% desc
    (10, 10, 95.0),     # 5% desc
    (5, 10, 50.0)       # 0% desc
])
def test_descuento_por_volumen_rangos(cantidad, precio_unitario, esperado):
    # Arrange / Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == esperado

def test_descuento_por_volumen_errores():
    # Arrange / Act / Assert
    with pytest.raises(ValueError, match="La cantidad no puede ser negativa"):
        descuento_por_volumen(-5, 10)
    with pytest.raises(ValueError, match="El precio unitario no puede ser negativo"):
        descuento_por_volumen(10, -10)

# --- Pruebas descuento_cumulativo ---
def test_descuento_cumulativo_valido():
    # Arrange
    precio, descuentos = 100, [10, 20]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 72.0

def test_descuento_cumulativo_sin_descuentos():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 100.0

def test_descuento_cumulativo_errores():
    # Arrange / Act / Assert
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        descuento_cumulativo(-100, [10])
    with pytest.raises(ValueError, match="Cada descuento debe estar entre 0 y 100"):
        descuento_cumulativo(100, [10, 120])

# --- Pruebas descuento_apilado ---
def test_descuento_apilado_normal():
    # Arrange
    precio, descuentos = 100, [10, 20]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 70.0

def test_descuento_apilado_sin_descuentos():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 100.0

def test_descuento_apilado_excede_100_porcentaje():
    # Arrange
    precio, descuentos = 100, [60, 50]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 0.0

def test_descuento_apilado_precio_negativo_lanza_error():
    # Arrange / Act / Assert
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        descuento_apilado(-100, [10])
