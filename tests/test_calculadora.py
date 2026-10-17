import pytest
from src.calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir,
    potencia,
    raiz_cuadrada,
    promedio,
    maximo,
    minimo,
    calcular_area_rectangulo,
    calcular_perimetro_rectangulo
)

# --- Pruebas Operaciones Básicas ---
def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12

def test_restar_positivos():
    # Arrange
    a, b = 10, 4
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == 6

def test_multiplicar_positivos():
    # Arrange
    a, b = 3, 4
    # Act
    resultado multiplicar(a, b)
    # Assert
    assert resultado == 12

def test_dividir_exitoso():
    # Arrange
    a, b = 20, 4
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 5.0

def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0
    # Act & Assert
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(a, b)

def test_potencia_valida():
    # Arrange
    base, exponente = 2, 3
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == 8

# --- Pruebas de Raíz Cuadrada ---
def test_raiz_cuadrada_numero_positivo():
    # Arrange
    numero = 16
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 4.0

def test_raiz_cuadrada_numero_negativo_lanza_error():
    # Arrange
    numero = -9
    # Act & Assert
    with pytest.raises(ValueError, match="No se puede calcular la raíz cuadrada de un número negativo"):
        raiz_cuadrada(numero)

# --- Pruebas de Promedio, Máximo y Mínimo ---
def test_promedio_lista_valida():
    # Arrange
    lista = [10, 20, 30]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 20.0

def test_promedio_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act & Assert
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        promedio(lista)

def test_maximo_lista_valida():
    # Arrange
    lista = [3, 9, 1, 5]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == 9

def test_maximo_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act & Assert
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        maximo(lista)

def test_minimo_lista_numeros_positivos():
    # Arrange
    numeros = [5, 10, 15]
    # Act
    resultado = minimo(numeros)
    # Assert
    assert resultado == 5

def test_minimo_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act & Assert
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        minimo(lista)

# --- Pruebas de Rectángulo ---
def test_calcular_area_rectangulo_valido():
    # Arrange
    base, altura = 5, 4
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 20

def test_calcular_area_rectangulo_negativo_lanza_error():
    # Arrange
    base, altura = -5, 4
    # Act & Assert
    with pytest.raises(ValueError, match="La base y altura deben ser positivas"):
        calcular_area_rectangulo(base, altura)

def test_calcular_perimetro_rectangulo_valido():
    # Arrange
    base, altura = 4, 5
    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)
    # Assert
    assert resultado == 18

def test_calcular_perimetro_rectangulo_negativo_lanza_error():
    # Arrange
    base, altura = 4, -5
    # Act & Assert
    with pytest.raises(ValueError, match="La base y altura deben ser positivas"):
        calcular_perimetro_rectangulo(base, altura)
