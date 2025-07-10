
pila_farmacia =[]
cola_medicamento=[]
medicina =""
while medicina !="salir":
   medicina=string(imput("ingrese lista de medicamento"))
   pila_farmacia.append(medicina)
   print("ingreso con éxito")

for i in pila_farmacia:
    cola_medicamento.append(i)

print("medicamento ingresado")
print(pila_farmacia)
print("despacho de medicamento")
print(cola_medicamento)