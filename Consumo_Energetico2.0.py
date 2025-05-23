"""
Autores: Andy, D. Joshua, D. Sahid, L.
Fecha: 20/05/2025
Versión: 1.0
Descripción: Programa que registra el consumo energético de 4 edificios del campus
universitario durante una semana. Se ingresan los kWh en 3 turnos diarios,
se calcula el consumo total por edificio y su promedio semanal.
"""

from array import array

# Parte 1
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
turnos_dia = ["Mañana", "Tarde", "Noche"]

# 4 edificios x 7 días x 3 turnos = 84 posiciones
consumo_edificios = array("f", [0.0] * 84)

def obtener_indice(edificio, dia, turno):
    # Fórmula para convertir 3D -> 1D
    return edificio * 21 + dia * 3 + turno

# Parte 2: Recolección de datos
for i in range(4):  # edificios
    print("*" * 50)
    print(f"--- Edificio {i + 1} ---")
    for j in range(7):  # días
        print(f"Día: {dias_semana[j]}")
        for k in range(3):  # turnos
            while True:
                try:
                    valor = float(input(f"Consumo en turno de {turnos_dia[k]} (kWh): "))
                    if valor < 0:
                        print("El valor debe ser positivo.")
                    else:
                        index = obtener_indice(i, j, k)
                        consumo_edificios[index] = valor
                        break
                except ValueError:
                    print("Debe ingresar un número válido.")

# Parte 3: Mostrar resultados
print("\n******* REGISTRO DEL CÁLCULO ******")
for i in range(4):  # edificios
    total = 0.0
    for j in range(7):  # días
        for k in range(3):  # turnos
            index = obtener_indice(i, j, k)
            total += consumo_edificios[index]
    promedio = total / 7
    print("#" * 50)
    print("********** Cálculo de consumo energético **********")
    print(f"Edificio {i + 1}:")
    print(f" - Consumo total semanal: {total:.2f} kWh")
    print(f" - Promedio diario: {promedio:.2f} kWh")
    print("********** ***************************** **********")
