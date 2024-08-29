class Consultorio:
    def __init__(self):
        self.paciente = ""
        self.DUI = ""
        self.motivo = ""
        self.fechaquellego = ""
        self.fechaasignada = ""
        
    def saladeespera(self):
        if self.programado.lower() == "si":
            print(f"El paciente {self.paciente} tiene una cita programada, vino el día {self.fechaquellego} y será pasado a sala de espera.")
        elif self.programado.lower() == "no":
            print(f"El paciente {self.paciente} tiene que volver el día establecido: {self.fechaasignada}.")
        else:
            print("Ingresa una respuesta correcta (si/no).")

    def registro(self):
        self.programado = input("¿El paciente ya tiene una cita programada? Escriba 'si' o 'no': ").strip().lower()
        if self.programado == "no":
            self.paciente = input("Ingrese el nombre del paciente: ")
            self.DUI = input("Ingrese el DUI: ")
            self.motivo = input("Escriba el motivo de consulta: ")
            self.fechaquellego = input("Escriba la fecha en que llegó el paciente: ")
            self.fechaasignada = input("Ingrese la fecha en que se le asignará la consulta: ")
        elif self.programado == "si":
            self.paciente = input("Se pasara a sala de espera")
        else:
            print("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")
    
    def mostrardato(self):
        print("--------------------------------------------")
        print("La salud es importante, y nosotros nos preocupamos por usted.")
        self.saladeespera()
        print("--------------------------------------------")
        print(f"Paciente que llegó hoy: {self.paciente}")
        print(f"DUI del paciente: {self.DUI}")
        print(f"Motivo de venir: {self.motivo}")
        print(f"Fecha en que vino para hacer su consulta: {self.fechaquellego}")
        print(f"Fecha asignada para pasar: {self.fechaasignada}")


orden = Consultorio()
orden.registro()
orden.mostrardato()
