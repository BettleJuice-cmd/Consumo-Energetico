Algoritmo consumoEnerg�tico20
	// Autores: Manuel Mayorga y Josue Reyes
	// Versi�n 1.1 
	// Programa para registrar el consumo energ�tico de 4 edificios durante una semana
	
	Definir edificios, edificio, dia, turno Como Entero
	Definir consumo, total_edificio, total_general, promedio_semanal Como Real
	
	edificios <- 4
	total_general <- 0
	
	Escribir "Registro de consumo energ�tico (kW) por edificio, d�a y turno"
	
	Para edificio <- 1 Hasta edificios Con Paso 1
		Escribir ""
		Escribir "--- Edificio ", edificio, " ---"
		total_edificio <- 0
		
		Para dia <- 1 Hasta 7 Con Paso 1
			Escribir ""
			Escribir "D�a ", dia
			
			Para turno <- 1 Hasta 3 Con Paso 1
				Escribir "  Consumo en turno ", turno, ": "
				Leer consumo
				total_edificio <- total_edificio + consumo
			Fin Para
		Fin Para
		
		promedio_semanal <- total_edificio / 7
		promedio_semanal <- Trunc(promedio_semanal * 100) / 100
		total_edificio <- Trunc(total_edificio * 100) / 100
		
		Escribir ""
		Escribir "=> Total consumido en Edificio ", edificio, ": ", total_edificio, " kW"
		Escribir "=> Promedio diario (semana): ", promedio_semanal, " kW/d�a"
		
		total_general <- total_general + total_edificio
	Fin Para
	
	total_general <- Trunc(total_general * 100) / 100
	
	Escribir ""
	Escribir "*** Consumo total de los ", edificios, " edificios: ", total_general, " kW ***"

FinAlgoritmo
