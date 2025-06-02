"""
Autor: Andy, D.
Fecha: 01/06/2025
Version: 1.0
Descripcion: Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de
la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por
sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por
sección, así como el total general de la semana. 
"""

dias_Semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
secciones = ["Sección A", "Sección B", "Sección C"]

asistencia=[]


for i in range(5):
    print("Día:", dias_Semana[i])
    for j in range(3):
        print("Asistencia de la seccion: ", secciones[j])
        seccion_Asistencia=[]
        for k in range[6]:
            Presente = input("El estudiante", k+1, "esta presente? (S/N): ")
            if Presente == "S":
                seccion_Asistencia.append("Presente")
                print("El estudiante", k+1, "esta presente")
            else:
                print("El estudiante", k+1, "esta ausente")
        print("Asistencia de la sección", secciones[j], "del día", dias_Semana[i], "registrada.")
    secciones.append()
    dias_Semana.append()

        
            
        
