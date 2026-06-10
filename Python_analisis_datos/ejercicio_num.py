# GUÍA DE TRABAJO PRÁCTICO INTEGRADOR
# Análisis de Datos Computacionales con NumPy

""" Contexto para el alumno: Te has incorporado como Científico de Datos en una reserva ecológica artificial
regulada tecnológicamente mediante un domo inteligente. Tu primera misión es procesar, limpiar y extraer
estadísticas clave de una matriz de datos crudos recolectados por los sensores de monitoreo ambiental."""

""" 1. Estructura de la Matriz de Datos
El sistema central genera un arreglo bidimensional (matriz) de NumPy donde cada fila representa un sensor
geográfico específico y cada columna almacena una variable ambiental crítica:
• Filas (Sensores): Fila 0 = Norte, Fila 1 = Sur, Fila 2 = Este, Fila 3 = Oeste.
• Columnas (Variables): Columna 0 = Temperatura (°C), Columna 1 = Humedad (%), Columna 2 = Nivel de CO₂ (ppm).

Ubicación Sensor    Columna 0: Temperatura (°C) Columna 1: Humedad (%)  Columna 2: CO₂ (ppm)
Sensor 0 (Norte)    24.5                    55.0                        380.0
Sensor 1 (Sur)      120.0 *                 60.0                        NaN (Vacío) *
Sensor 2 (Este)     21.2                    -999.0 *                    410.0
Sensor 3 (Oeste)    26.8                    48.0                        395.0

* Nota: Los valores marcados representan fallas o anomalías operativas del sistema de captura que requieren saneamiento inmediato."""

""" 2. Código Base Inicial
Copia y ejecuta el siguiente bloque de código en tu entorno de desarrollo para inicializar la matriz con los
datos corruptos del reporte de sensores:"""

import numpy as np
# Matriz cruda: 4 sensores (filas) x 3 variables de entorno (columnas)
datos_ambientales = np.array([
    [24.5, 55.0,    380.0],  # Norte
    [120.0, 60.0,   np.nan], # Sur (Fallo térmico y dato faltante)
    [21.2, -999.0, 410.0],   # Este (Fallo de sensor de humedad)
    [26.8, 48.0,    395.0]   # Oeste
])
print("--- MATRIZ ORIGINAL DE SENSORES ---")
print(datos_ambientales)