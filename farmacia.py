
pila_farmacia = []
cola_medicamento = []
medicina = ""
op =int(input())
print("Ingreso Medicamento")
print("entrega de medicamento")
print("mostrar Pila actual")
print("salir")
match op!=4:
    case 1 :



while medicina != "salir":
    medicina = input("Ingrese nombre del medicamento (o escriba 'salir' para terminar): ")
    if medicina == "salir":
        print("Saliendo del ingreso de medicamentos.")
    else:
        pila_farmacia.append(medicina)
        print("Ingreso con éxito.")

# Transferir de la pila a la cola (en el mismo orden que se ingresaron)
for i in pila_farmacia:
    cola_medicamento.append(i)
    cola_invertida = cola_medicamento[::-1]

print("\nMedicamentos ingresados (Pila):")
print(pila_farmacia)

print("\nDespacho de medicamentos (Cola):")
print(cola_invertida)

