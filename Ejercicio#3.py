"""
Autores: Andy, D. Joshua, D. Sahid, L.
Fecha: 01/06/2025
Version: 1.0
Descripcion: Cree un programa que permita llevar un registro
de ventas en una feria estudiantil organizada
por la UAM. La feria se desarrollará durante tres días,
con cuatro stands por día. Cada stand ofrecerá tres productos distintos.
 El sistema deberá permitir ingresar el monto de venta por
producto y mostrar un resumen por stand, por día, y un total general de la feria.
"""

DIAS = 3
STANDS_POR_DIA = 4
PRODUCTOS_POR_STAND = 3


ventas = []


for dia in range(DIAS):
    print(f"\n--- Día {dia + 1} ---")
    dia_ventas = []
    for stand in range(STANDS_POR_DIA):
        print(f"\n  Stand {stand + 1}:")
        stand_ventas = []
        for producto in range(PRODUCTOS_POR_STAND):
            while True:
                try:
                    monto = float(input(f"    Ingrese monto de venta del Producto {producto + 1}: "))
                    break
                except ValueError:
                    print("    Entrada inválida. Ingrese un número válido.")
            stand_ventas.append(monto)
        dia_ventas.append(stand_ventas)
    ventas.append(dia_ventas)


total_general = 0
for dia in range(DIAS):
    print(f"\n**** Resumen Día {dia + 1} ****")
    total_dia = 0
    for stand in range(STANDS_POR_DIA):
        total_stand = sum(ventas[dia][stand])
        print(f"  Stand {stand + 1} - Total ventas: ${total_stand:.2f}")
        total_dia += total_stand
    print(f"Total del Día {dia + 1}: ${total_dia:.2f}")
    total_general += total_dia

print(f"\n**** Total General de la Feria: ${total_general:.2f} ***")