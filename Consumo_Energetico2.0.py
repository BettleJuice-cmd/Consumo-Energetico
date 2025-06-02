"""
Autores: Andy, D. Joshua, D. Sahid, L.
Fecha: 20/05/2025
Versión: 2.0
Descripción: Programa que registra el consumo energético de 4 edificios del campus
universitario durante una semana. Se ingresan los kWh en 3 turnos diarios,
se calcula el consumo total por edificio y su promedio semanal.
"""
#Parte 1

#Se importa el modulo de arrelos llamado "Array"
from array import array

# Se crean las listas
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
turnos_dia = ["Mañana", "Tarde", "Noche"]

# Se inicializa un arreglo para el almacenamiento de los datos de consumo (4 edificios x 7 días x 3 turnos = 84 posiciones)
consumo_edificios = array("f", [0.0] * 84)  #Este es el arreglo

def obtener_indice(edificio, dia, turno):
    # Fórmula para convertir los datos recopilados en el bucle
    return edificio * 21 + dia * 3 + turno

# Parte 2
# En esta parte se recopilan los datos. Se le pide al usuario que ingrese los datos de consumo por cada turno del dia
for i in range(4):  # Bucle de edificios
    print("*" * 50)
    print(f"--- Edificio {i + 1} ---")
    for j in range(7):  # Bucles de dias
        print(f"Día: {dias_semana[j]}")
        for k in range(3):  # Bucle de turnos
            while True:  # En esta parte se verifica si los datos ingresados por el usuario son de tipo float, positivos y que no sean caracteres
                try:
                    valor = float(input(f"Consumo en turno de {turnos_dia[k]} (kWh): "))
                    if valor < 0:
                        print("El valor debe ser positivo.")
                    else:
                        index = obtener_indice(i, j, k)
                        consumo_edificios[index] = valor
                        break
                except ValueError:
                    print("Debe ingresar un número válido.") # Si los datos son incorrectos, se les mostrara este comentario al usuario

# Parte 3
# Se resuelven todos los valores y se calcula el promedio semanal y promedio diario por edificio

print("\n******* REGISTRO DEL CÁLCULO ******")
for i in range(4):  # Bucle de edificios
    total = 0.0
    for j in range(7):  # días
        for k in range(3):  # turnos
            index = obtener_indice(i, j, k) #Index calcula la posicion exacta dentro del arreglo consumo_edificios  
            total += consumo_edificios[index]
    promedio = total / 7 #Formula para calcular el promedio diario

    #Ficha de salida de datos
    print("#" * 50)
    print("********** Cálculo de consumo energético **********")
    print(f"Edificio {i + 1}:")
    print(f" - Consumo total semanal: {total:.2f} kWh")
    print(f" - Promedio diario: {promedio:.2f} kWh")
    print("********** ***************************** **********")
