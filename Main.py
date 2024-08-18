class Auto:
    def __init__(self, placa, marca, modelo, descripcion, precioUnitario):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precioUnitario = precioUnitario


class Cliente:
    def __init__(self, nombre, correoElectronico, nit):
        self.nombre = nombre
        self.correoElectronico = correoElectronico
        self.nit = nit


class Compra:
    idCompra = 0

    def __init__(self, listaAutos, cliente, total=0):
        Compra.idCompra += 1
        self.id = Compra.idCompra
        self.listaAutos = listaAutos
        self.cliente = cliente
        self.total = total


class Main:
    def __init__(self):

        self.autos = []
        self.clientes = []
        self.compras = []

        cliente1 = Cliente("Fulano", "correo@ejemplo.com", "123456789")
        cliente2 = Cliente("Mengano", "correo2@ejemplo.com", "133256485")
        self.clientes.append(cliente1)
        self.clientes.append(cliente2)

        auto1 = Auto("P123ABC", "Toyota", "Corolla", "Descripción del auto 1", 25000.00)
        auto2 = Auto("P456DEF", "Honda", "Civic", "Descripción del auto 2", 36000.00)
        self.autos.append(auto1)
        self.autos.append(auto2)

        compra1 = Compra([auto1, auto2], cliente1, 61000.00)
        self.compras.append(compra1)


    def desplegarMenu(self):
        while True:
            print("\n------------- Menú Principal -------------")
            print("1. Registrar Auto\n2. Registrar Cliente\n3. Realizar Compra\n4. Reporte de Compras\n5. Datos del Estudiante\n6. Salir")
            print("------------------------------------------\n")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrarAuto()
            elif opcion == "2":
                self.registrarCliente()
            elif opcion == "3":
                self.realizarCompra()
            elif opcion == "4":
                self.reporteDeCompras()
            elif opcion == "5":
                self.datosDelEstudiante()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def registrarAuto(self):
        placa = input("Ingrese la placa del auto: ")
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        descripcion = input("Ingrese la descripción del auto: ")
        precio = float(input("Ingrese el precio del auto: "))
        self.autos.append(Auto(placa, marca, modelo, descripcion, precio))
        print("Se ha registrado el auto con placa: ", placa, " exitosamente.")

    def registrarCliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        correo = input("Ingrese el correo electrónico del cliente: ")
        nit = input("Ingrese el NIT del cliente: ")
        self.clientes.append(Cliente(nombre, correo, nit))
        print("Se ha registrado el cliente con NIT: ", nit, " exitosamente.")

    def realizarCompra(self):
        nitCliente = input("Ingrese el NIT del cliente: ")
        cliente = next((c for c in self.clientes if c.nit == nitCliente), None)

        if cliente is None:
            print("El NIT ingresado no corresponde a ningún cliente registrado.")
            return

        autosComprados = []

        while True:
            print("\n-------------- Menú Compra --------------")
            print("1. Agregar Auto\n2. Terminar Compra y Generar Factura")
            print("-----------------------------------------\n")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                placaAuto = input("Ingrese la placa del auto: ")
                auto = next((a for a in self.autos if a.placa == placaAuto), None)

                if auto is None:
                    print("La placa ingresada no corresponde a ningún auto registrado.")
                else:
                    autosComprados.append(auto)
            elif opcion == "2":
                if not autosComprados:
                    print("No se ha agregado ningún auto a la compra.")
                else:
                    self.generarFactura(autosComprados, cliente)
                    break
            else:
                print("Opción no válida. Intente de nuevo.")

    def generarFactura(self, autosComprados, cliente):
        seguro = input("¿Desea agregar seguro a los autos comprados? (SI/NO): ")

        if seguro.upper() == "SI":
            total = sum(auto.precioUnitario + auto.precioUnitario * 0.15 for auto in autosComprados)
        elif seguro.upper() == "NO":
            total = sum(auto.precioUnitario for auto in autosComprados)
        else:
            print("Opción no válida. Intente de nuevo.")
            return

        compra = Compra(autosComprados, cliente, total)
        self.compras.append(compra)
        print(f"Compra realizada y factura generada. Total: Q{total}")

    def reporteDeCompras(self):
        print("\n-------------- REPORTE DE COMPRAS --------------")
        print("================================================")

        if not self.compras:
            print("No se han realizado compras.")
            print("------------------------------------------------")
            return

        totalGeneral = 0
        for compra in self.compras:
            print("CLIENTE:")
            print(f"Nombre: {compra.cliente.nombre}")
            print(f"Correo electrónico: {compra.cliente.correoElectronico}")
            print(f"Nit: {compra.cliente.nit}")
            print("\nAUTO(S) ADQUIRIDO(S):")
            for auto in compra.listaAutos:
                print(f"Placa: {auto.placa}, \nMarca: {auto.marca}, \nModelo: {auto.modelo}, \nPrecio: Q{auto.precioUnitario}, \nDescripción: {auto.descripcion}, \n")
            print(f"\nID de Compra: {compra.id}")
            print(f"\nTOTAL: Q{compra.total}")
            print("==============================================")
            totalGeneral += compra.total

        print(f"Total General: Q{totalGeneral}")
        print("------------------------------------------------")

    def datosDelEstudiante(self):
        print("Nombre: Xavi Alexander De León Perdomo")
        print("Carné: 202300596")
        print("Introducción a la Programación y Computación 2 Sección: A")
        print("4to. Semestre")
    
    
if __name__ == "__main__":

    main = Main()
    main.desplegarMenu()