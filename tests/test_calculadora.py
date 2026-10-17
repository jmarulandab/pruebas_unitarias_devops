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


def test_sumar_positivos():
   
    a, b = 7, 5
    
    resultado = sumar(a, b)
    
    assert resultado == 12

def test_restar_positivos():
    
    a, b = 10, 4
    
    resultado = restar(a, b)
    
    assert resultado == 6


def test_dividir_por_cero_lanza_error():

    a, b = 10, 0
   
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(a, b)

# --- ( BUG 1) ---
def test_raiz_cuadrada_numero_positivo():
    
    numero = 16
   
    resultado = raiz_cuadrada(numero)
    
    assert resultado == 4.0

def test_raiz_cuadrada_numero_negativo_lanza_error():
    
    numero = -9
    
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)

# --- ( BUG 2) ---
def test_minimo_lista_numeros_positivos():
    
    numeros = [5, 10, 15]
    
    resultado = minimo(numeros)
    
    assert resultado == 5


def test_calcular_perimetro_rectangulo_valido():
    
    base, altura = 4, 5
    
    resultado = calcular_perimetro_rectangulo(base, altura)
    
    assert resultado == 18
