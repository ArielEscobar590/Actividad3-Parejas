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

def main():
    nombre = input("Ingrese el nombre del cliente: ")
    edad = input("Ingrese el edad del cliente: ")
    padeciemiento = input("Ingrese el padeciemiento del cliente: ")
    cliente = Cliente(nombre, edad, padeciemiento)
