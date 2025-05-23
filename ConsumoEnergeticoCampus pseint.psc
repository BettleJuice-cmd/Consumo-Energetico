Algoritmo ConsumoEnergeticoCampus
    // Definición de variables y estructuras
    Definir dias_semana Como Cadena
    Dimension dias_semana[7]
    dias_semana[0] <- "Lunes"
    dias_semana[1] <- "Martes"
    dias_semana[2] <- "Miércoles"
    dias_semana[3] <- "Jueves"
    dias_semana[4] <- "Viernes"
    dias_semana[5] <- "Sábado"
    dias_semana[6] <- "Domingo"
    
    Definir turnos_dia Como Cadena
    Dimension turnos_dia[3]
    turnos_dia[0] <- "Mañana"
    turnos_dia[1] <- "Tarde"
    turnos_dia[2] <- "Noche"
    
    // Matriz para almacenar los consumos (4 edificios x 7 días x 3 turnos)
    Definir consumo_edificios Como Real
    Dimension consumo_edificios[4,7,3]
    
    // Variables para los bucles
    Definir i, j, k Como Entero
    Definir valor Como Real
    
    // Parte 1: Recopilación de datos
    Para i <- 0 Hasta 3 Hacer // 4 edificios (0-3)
        Escribir "******************************************"
        Escribir "--- Edificio ", i+1, " ---"
        
        Para j <- 0 Hasta 6 Hacer // 7 días (0-6)
            Escribir "Día: ", dias_semana[j]
            
            Para k <- 0 Hasta 2 Hacer // 3 turnos (0-2)
                Escribir "  Consumo en turno de ", turnos_dia[k], " (kWh): " Sin Bajar
                Leer valor
                consumo_edificios[i,j,k] <- valor
            FinPara
        FinPara
        
        Escribir "******************************************"
    FinPara
    
    // Parte 2: Procesamiento y resultados
    Escribir ""
    Escribir "******* REGISTRO DEL CÁLCULO ******"
    
    Para i <- 0 Hasta 3 Hacer
        Definir total Como Real
        total <- 0
        
        // Calcular consumo total del edificio
        Para j <- 0 Hasta 6 Hacer
            Para k <- 0 Hasta 2 Hacer
                total <- total + consumo_edificios[i,j,k]
            FinPara
        FinPara
        
        // Calcular promedio
        Definir promedio Como Real
        promedio <- total / 7
        
        // Mostrar resultados
        Escribir "##########################################"
        Escribir "********** Cálculo de consumo energético **********"
        Escribir "Edificio ", i+1, ":"
        Escribir " - Consumo total semanal: ", total, " kWh"
        Escribir " - Promedio diario: ", promedio, " kWh"
        Escribir ""
        Escribir "******************************************"
        Escribir "##########################################"
    FinPara
    
    Escribir "Fin del programa"
FinAlgoritmo