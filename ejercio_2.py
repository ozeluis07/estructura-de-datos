import os 
os.system("cls")
ventas = []
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

for dia in dias:
    monto = float(input("Ventas del " + dia + ": "))
    ventas.append(monto)

total = sum(ventas)
promedio = total / len(ventas)
venta_mayor = max(ventas)

posicion = ventas.index(venta_mayor)
dia_mayor = dias[posicion]

print("\nResultados:")
print("Total de la semana:", total)
print("Promedio diario:", promedio)
print("el dia con mayor venta fue el ", dia_mayor, "con un monto de ", venta_mayor)