cantidad = int(input("Cuantos dias quieres registrar? "))
temperaturas = []

for i in range(cantidad):
    temp = float(input("Temperatura del dia " + str(i + 1) + ": "))
    temperaturas.append(temp)

calientes = []
for t in temperaturas:
    if t > 30:
        calientes.append(t)

print("\nTodas las temperaturas:", temperaturas)
print("Temperaturas mayores a 30 grados:", calientes)
print("Hubo", len(calientes), "dias de mucho calor.")