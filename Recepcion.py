class Cliente:
    def __init__(self, nombre, edad, padeciemiento):
        self.nombre = nombre
        self.edad = edad
        self.padeciemiento = padeciemiento
        self.clientes = []

    def agregarCliente(self, cliente):
        self.clientes.append(cliente)

    def listaClientes(self):
        for cliente in self.clientes:
            a = 1
            print(f"{a}) {cliente.nombre}, {cliente.edad}, {cliente.padeciemiento}")
            a += 1

    def eliminarCliente(self, cliente):
        self.clientes.remove(cliente)


def main():
    while True:
        cli = cliente()
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
        elif op == "2":
            cli.listaClientes()
        elif op == "3":
            cli.eliminarCliente(cliente)
        elif op == "4":
            print("Gracias por usar el sistema. Nos vemos")
            break

