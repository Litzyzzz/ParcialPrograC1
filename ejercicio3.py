"""
Un hotel de playa cuenta con un recepcionista que se encarga de
presentar a los clientes las opciones de habitaciones disponibles junto
con sus precios. Tras la elección de la habitación, el recepcionista
solicita los datos personales del cliente y el número de noches que
permanecerá en el hotel. Finalmente, entrega al cliente una factura
detallada con el total de los gastos.
 Adicionalmente, los clientes pueden solicitar servicios extra,
como el uso de la piscina o la cancha de golf, que tienen un costo
adicional. Implementa esta funcionalidad en tu programa
""" 

class Hotel:
    def __init__(self):
        self.nombreCliente = ""
        self.telefonoCliente = ""
        self.numNoches = 0
        self.tipoHabitacion = ""
        self.servicioExtra = ""
        self.totalGastos = 0
        self.cobroServicioExtra = 0

        self.__precio1 = 85   
        self.__precio2 = 115  
        self.__precio3 = 185  

        self.__servicioPiscina = 10  
        self.__servicioBar = 50      

    def datosCliente(self):
        self.tipoHabitacion = input("Tipo de Habitación a escoger. (Individual/Doble/Suite): ").capitalize()
        if self.tipoHabitacion in ["Individual", "Doble", "Suite"]:
            self.nombreCliente = input("Nombre del cliente: ")
            self.telefonoCliente = input("Número del cliente: ")
            self.numNoches = int(input("Noches a permanecer: "))
            self.servicioExtra = input("¿Desea usar servicios extras? (Piscina/Bar/Ninguno): ").capitalize()
        else:
            print("Tipo de habitación no válido.")

    def calcularTotalGastos(self):
        if self.tipoHabitacion == "Individual":
            self.totalGastos = self.numNoches * self.__precio1
        elif self.tipoHabitacion == "Doble":
            self.totalGastos = self.numNoches * self.__precio2
        elif self.tipoHabitacion == "Suite":
            self.totalGastos = self.numNoches * self.__precio3

        if self.servicioExtra == "Piscina":
            self.cobroServicioExtra = self.__servicioPiscina
        elif self.servicioExtra == "Bar":
            self.cobroServicioExtra = self.__servicioBar
        else:
            self.cobroServicioExtra = 0

        self.totalGastos += self.cobroServicioExtra

    def mostrarFactura(self):
        self.calcularTotalGastos()
        if self.tipoHabitacion in ["Individual", "Doble", "Suite"]:
            print("\n----- Factura -----")
            print(f"Tipo de habitación: {self.tipoHabitacion}")
            print(f"Nombre del Cliente: {self.nombreCliente}")
            print(f"Número de teléfono: {self.telefonoCliente}")
            print(f"Gasto total: ${self.totalGastos}")
            if self.servicioExtra in ["Piscina", "Bar"]:
                print(f"Servicio extra: {self.servicioExtra} (${self.cobroServicioExtra})")
            else:
                print("No se seleccionaron servicios extras.")
            print("--------------------")


cliente1 = Hotel()
cliente1.datosCliente()
cliente1.mostrarFactura()







        
        
       


        
            
            
            
                

            
            
        


    

