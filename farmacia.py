
pila_farmacia =[]
cola_medicamento=[]
medicina =""
while medicina !="salir":
    medicina = input("ingrese lista de medicamento")
    if medicina == "salir":
          print("salir de ingreso")
    else:
       pila_farmacia.append(medicina)
       print("ingreso con éxito")

for i in pila_farmacia:
    cola_medicamento.append(i)

print("medicamento ingresado")
print(pila_farmacia)
print("despacho de medicamento")
print(cola_medicamento)