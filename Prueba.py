"""
Nombre: Andy, D.
Fecha: 20/05/2025
Version: 1.0
Descripcion: Desarrolle un programa que registre el consumo energético de cuatro edificios del campus 
universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en 
tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y 
generar el promedio semanal correspondiente.
"""


#Parte 1

# Definir las listas

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"] #Creamos una lista con los dias de la semana "
turnos_dia = ["Mañana", "Tarde", "Noche"] #Creamos otra lista con los turnos del dia


#Crear una lista que almacene los datos recopilados por edificio
consumo_edificios = []

#Parte 2
# Crear los bucles para la recopilacion de los datos junto a la pantalla que se mostrara al usuario
for i in range(4): # Son 4 edificios
    print("*"*50)
    print(f"--- Edificio {i + 1} ---") #Se le suma 1 al edificio para que se empiece a contar desde "Edificio 1"
    edificio=[]
    for j in range(7): # Son 7 dias
       print(f" Dia: {dias_semana[j]}")
       dia = []
       for k in range(3): #Son los tres turnos del dia: Mañana, Tarde y Noche
            valor = float(input(f"  Consumo en turno de {turnos_dia[k]} (kWh): ")) #Se pide el consumo por cada turno al usuario
            dia.append(valor)
       edificio.append(dia)
    print("*"*50)
    consumo_edificios.append(edificio)

# Parte 3
# Procesar y mostrar los resultados 
print("\n******* REGISTRO DEL CÁLCULO *******")
for i in range(4):
    total = 0
    for j in range(7):
        total += sum(consumo_edificios[i][j])  #Sumamos el consumo de cada turno por dia
    promedio = total / 7  #Calculamos el promedio semanal
    # Mostrar resultados
    print("#"*50)
    print("********** Calculo de consumo energetico **********")
    print(f"Edificio {i + 1}:")
    print(f" - Consumo total semanal: {total:.2f} kWh")
    print(f" - Promedio diario: {promedio:.2f} kWh\n")
    print("********** ***************************** **********")
    print("#"*50)
    #Fin del programa
