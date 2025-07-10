class Cliente:
    def __init__(self, nombre, edad, padeciemiento):
        self.nombre = nombre
        self.edad = edad
        self.padeciemiento = padeciemiento

class Recepcion:
    def __init__(self):
        self.listaclientes = []

    def agregarCliente(self, cliente):
        self.listaclientes.append(cliente)
        print("Cliente agregada exitosamente")

    def listaClientes(self):
        if(len(self.listaclientes) == 0):
            print("No hay clientes")
        else:
            for cliente in self.listaclientes:
                a = 1
                print(f"{a}) {cliente.nombre}, {cliente.edad}, {cliente.padeciemiento}")
                a += 1

    def eliminarCliente(self):
        if(len(self.listaclientes) == 0):
            print("No hay clientes para atender")
        else:
            print(f"{self.listaclientes[0].nombre} ha sido atendido exitosamente")
            del self.listaclientes[0]



def menu():
    recepcion = Recepcion()
    while True:
        try:
            print("--- Recepcion ---")
            print("1. Agregar Cliente")
            print("2. Listar Clientes")
            print("3. Atender Clientes")
            print("4. Salir")
            op = input("Ingrese una opcion: ")
            if op == "1":
                nombre = input("Ingrese el nombre del cliente: ")
                edad = input("Ingrese el edad del cliente: ")
                padeciemiento = input("Ingrese el padeciemiento del cliente: ")
                cliente = Cliente(nombre, edad, padeciemiento)
                recepcion.agregarCliente(cliente)
            elif op == "2":
                   recepcion.listaClientes()
            elif op == "3":
                   recepcion.eliminarCliente()
            elif op == "4":
                print("Gracias por usar el sistema. Nos vemos")
                break
        except:
            print("Ingreso no valida")
menu()