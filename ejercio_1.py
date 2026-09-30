
inventario = ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora", "Router", "Webcam", "Audifonos"]

print("Inventario inicial:")
for producto in inventario:
    print("-", producto)

nuevo = input("\nEscribe el producto que quieres agregar: ")
inventario.append(nuevo)
print("Producto agregado.")

# Modificar un producto existente
print("\nLista actual con posiciones:")
for i in range(len(inventario)):
    print(i, "-", inventario[i])

posicion = int(input("\nEscribe la posicion del producto que quieres cambiar: "))
if posicion >= 0 and posicion < len(inventario):
    nuevo_nombre = input("Escribe el nuevo nombre: ")
    inventario[posicion] = nuevo_nombre
    print("Producto modificado.")
else:
    print("Esa posicion no existe.")

print("\nInventario final:")
for producto in inventario:
    print("-", producto)