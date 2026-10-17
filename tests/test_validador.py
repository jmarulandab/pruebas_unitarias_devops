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

# --- Pruebas validar_email ---
def test_validar_email_casos():
    # Arrange / Act / Assert
    assert validar_email("estudiante@unal.edu.co") is True
    assert validar_email("") is False
    assert validar_email("email_sin_arroba.com") is False
    assert validar_email("dos@@arrobas.com") is False
    assert validar_email("@sinusuario.com") is False
    assert validar_email("sindominio@") is False
    assert validar_email("usuario@dominio_sin_punto") is False

# --- Pruebas validar_telefono ---
def test_validar_telefono_casos():
    # Arrange / Act / Assert
    assert validar_telefono("300-123-4567") is True
    assert validar_telefono("300 123 4567") is True
    assert validar_telefono("") is False
    assert validar_telefono("300ABC1234") is False
    assert validar_telefono("123") is False          # Corto (<7)
    assert validar_telefono("1234567890123456") is False # Largo (>15)

# --- Pruebas validar_edad ---
def test_validar_edad_casos():
    # Arrange / Act / Assert
    assert validar_edad(25) is True
    assert validar_edad("veinte") is False
    assert validar_edad(-5) is False
    assert validar_edad(130) is False

# --- Pruebas validar_password ---
def test_validar_password_casos():
    # Arrange / Act / Assert
    assert validar_password("DevOps2026!") is True
    assert validar_password("") is False
    assert validar_password("Short1!") is False      # Menos de 8 chars
    assert validar_password("sinmayuscula123") is False
    assert validar_password("SINMINUSCULA123") is False
    assert validar_password("SinNumeros!") is False

# --- Pruebas validar_url ---
def test_validar_url_casos():
    # Arrange / Act / Assert
    assert validar_url("https://github.com") is True
    assert validar_url("http://unal.edu.co") is True
    assert validar_url("") is False
    assert validar_url("ftp://servidor.com") is False

# --- Pruebas validar_fecha ---
def test_validar_fecha_casos():
    # Arrange / Act / Assert
    assert validar_fecha(15, 10, 2026) is True
    assert validar_fecha("15", 10, 2026) is False
    assert validar_fecha(15, 10, 1800) is False      # Año < 1900
    assert validar_fecha(15, 10, 2200) is False      # Año > 2100
    assert validar_fecha(31, 2, 2026) is False       # 31 Febrero inexistente

# --- Pruebas validar_cedula ---
def test_validar_cedula_casos():
    # Arrange / Act / Assert
    assert validar_cedula("1012345678") is True
    assert validar_cedula(1012345678) is True
    assert validar_cedula("") is False
    assert validar_cedula("10123ABC") is False
    assert validar_cedula("12345") is False           # < 6 dígitos
    assert validar_cedula("123456789012") is False     # > 10 dígitos
