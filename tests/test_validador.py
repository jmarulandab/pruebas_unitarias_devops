import pytest
from src.validador import (
    validar_email,
    validar_telefono,
    validar_edad,
    validar_password,
    validar_url,
    validar_fecha,
    validar_cedula
)

# --- Pruebas de Email y Teléfono ---
def test_validar_email_valido():
    # Arrange
    email = "estudiante@unal.edu.co"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is True

def test_validar_telefono_valido():
    # Arrange
    telefono = "300-123-4567"
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is True

# --- Pruebas de Contraseña y Edad ---
def test_validar_password_valida():
    # Arrange
    clave = "DevOps2026!"
    # Act
    resultado = validar_password(clave)
    # Assert
    assert resultado is True

def test_validar_edad_negativa_invalida():
    # Arrange
    edad = -5
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is False

# --- Pruebas de Fecha (Revela el BUG) ---
def test_validar_fecha_31_de_febrero_invalido():
    # Arrange
    dia, mes, año = 31, 2, 2026  # Febrero no tiene 31 días
    # Act
    resultado = validar_fecha(dia, mes, año)
    # Assert (Debe ser False)
    assert resultado is False
