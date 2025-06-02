
import os



"""
Autor: Andy D, Joshua D, Sahid L.
Fecha: 01/06/2025
Version: 1.0
Descripcion: Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de
la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por
sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por
sección, así como el total general de la semana. 
"""
# Definicion de las variables y listas necesarias

dias_Semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
secciones = ["Sección A", "Sección B", "Sección C"]

asistencia = []

# Se muestra un encabezado para el usuario
print("**************************************************************")
print("                    UNIVERSIDAD AMERICA                       ")
print("**************************************************************")
print("         Registro de Asistencia Semanal de Estudiantes        ") 



# Se desarrollan los bucles para obtener los datos de asistencia
# Por cada estudiante, para cada sección, y para cada día.

for i in range(5): 
    print("Día:", dias_Semana[i])
    dia_asistencia = []  
    for j in range(3):  
        print("Asistencia de la sección:", secciones[j])
        seccion_Asistencia = []
        for k in range(6):  
            respuesta = input(f"¿El estudiante {k+1} está presente? (S/N): ")
            if respuesta.upper() == "S":
                seccion_Asistencia.append(True)
            else:
                seccion_Asistencia.append(False)
        dia_asistencia.append(seccion_Asistencia)
    asistencia.append(dia_asistencia)

# Se limpia todo el alboroto
os.system("cls")  


# Se crean los contadores para cada sección, y un contador general
totales_por_seccion = [0, 0, 0]
total_general = 0

# Calcular totales de asistencia por sección y total general
for dia in asistencia:
    for i in range(len(secciones)):
        asistencias_seccion = sum(dia[i])  # cuenta los True en la sección i
        totales_por_seccion[i] += asistencias_seccion
        total_general += asistencias_seccion


# Se muestra nuevamente el encabezado, junto con los resultados
print("**************************************************************")
print("                    UNIVERSIDAD AMERICA                       ")
print("**************************************************************")
print("         Registro de Asistencia Semanal de Estudiantes        ") 
print("\nRESUMEN DE ASISTENCIAS:")
for i in range(len(secciones)):
    print(f"{secciones[i]}: {totales_por_seccion[i]} asistencias TOTALES de la semana")

print(f"Total general de asistencias en la semana: {total_general}")
 
