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
            print(f"{cliente.nombre}, {cliente.edad}, {cliente.padeciemiento}")
