# Informe de Taller: Análisis y Mejora de Pruebas Unitarias

**Asignatura:** Introducción a DevOps  
**Profesor:** Cesar Augusto Palacios Alarcón  
**Universidad:** Universidad Nacional de Colombia - Sede Manizales  
**Estudiante:** Juan Jose Marulanda Bustamante  
**Fecha:** Octubre 2026  

---

## 1. Análisis por Módulo

### `src/calculadora.py`
* **Descripción:** Proporciona funciones matemáticas y geométricas básicas (suma, resta, multiplicación, división, potencia, raíz cuadrada, promedio, máximo, mínimo, área y perímetro de rectángulo).
* **Estrategia de Pruebas (Criterio):** Se diseñaron pruebas en estructura AAA evaluando tanto flujos normales (operaciones con números positivos) como casos límite y de manejo de excepciones (división por cero, raíz cuadrada de números negativos, listas vacías en agregaciones y dimensiones negativas en figuras geométricas).

### `src/descuentos.py`
* **Descripción:** Gestiona la lógica comercial de promociones, aplicación de descuentos individuales, por volumen, acumulativos y apilados, así como el cálculo del precio final con impuestos.
* **Estrategia de Pruebas (Criterio):** Se probaron los rangos de porcentaje ($0\%$ a $100\%$), límites de volúmenes de compra ($\ge 100, 50, 20, 10$ unidades), la validación de montos o porcentajes negativos, y la secuencia matemática correcta al combinar descuentos con impuestos.

### `src/validador.py`
* **Descripción:** Módulo encargada de la validación de cadenas de texto y formatos comunes (correos electrónicos, números telefónicos, edades, contraseñas, URLs, fechas y cédulas).
* **Estrategia de Pruebas (Criterio):** Se priorizaron pruebas sobre casos de borde de entrada (cadenas vacías, tipos de datos inválidos, formatos incorrectos de email/URL) y en particular la validez real de días en calendarios (comprobación de límites de días por mes y años bisiestos).

---

## 2. Tabla de Bugs Encontrados y Corregidos

| Módulo | Función | Entrada que lo revela | Resultado Erróneo vs. Esperado | Corrección Aplicada |
| :--- | :--- | :--- | :--- | :--- |
| `calculadora.py` | `raiz_cuadrada` | `numero = -9` | **Erróneo:** Retornaba un número complejo `(0+3j)`.<br>**Esperado:** Lanzar excepción `ValueError`. | Se agregó validación `if numero < 0: raise ValueError(...)`. |
| `calculadora.py` | `minimo` | `lista = [5, 10, 15]` | **Erróneo:** Retornaba `0` (inicialización rígida).<br>**Esperado:** Retornar `5`. | Se cambió la inicialización de `min_val` a `lista[0]`. |
| `calculadora.py` | `calcular_perimetro_rectangulo` | `base=4, altura=5` | **Erróneo:** Retornaba `None` por falta de `return`.<br>**Esperado:** Retornar `18`. | Se añadió `return 2 * (base + altura)`. |
| `descuentos.py` | `calcular_precio_final` | `precio=100, impuesto=19, descuento=10` | **Erróneo:** Retornaba `109.0` (calculaba impuesto sobre base).<br>**Esperado:** Retornar `107.1` (impuesto sobre subtotal con descuento). | Se corrigió para calcular `impuesto_monto` sobre `precio_con_descuento`. |
| `descuentos.py` | `descuento_apilado` | `precio=100, descuentos=[60, 50]` | **Erróneo:** Permitía descuentos $>100\%$ generando valores inconsistentes.<br>**Esperado:** Limitar el descuento total a $100\%$ ($0.0$). | Se agregó tope `if total_descuento > 100: total_descuento = 100`. |
| `validador.py` | `validar_fecha` | `dia=31, mes=2, año=2026` | **Erróneo:** Retornaba `True` por validar solo el rango $1..31$.<br>**Esperado:** Retornar `False` (día inexistente en febrero). | Se implementó validación mediante `datetime(año, mes, dia)` dentro de bloque `try-except`. |

---

## 3. Cobertura de Código

### Reporte de Consola (`pytest-cov`)

```text
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
src/calculadora.py          44      0   100%
src/descuentos.py           60      0   100%
src/validador.py            65      0   100%
------------------------------------------------------
TOTAL                      169      0   100%
