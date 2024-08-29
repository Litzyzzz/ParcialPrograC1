"""
Esta clase nos ayudara como molde para los datos que necesitaremos de la biblioteca y de los alumnos 
que haran una orden, junto con datos importante como la sancion base que seria 10, esa sancion luego se 
multiplicara para conocer la cantidad de dinero que debe dar el multado
"""

class Biblioteca:
    def __init__(self):
        self.alumno = ""
        self.codigo = 0
        self.libro = ""
        self.fecha = ""
        self.carrera = ""
        self.fechaentrega = ""
        self.sancion = 10  
        self.meses_retraso = 0
#Esta funcion nos servira para calcular la cantidad de dinero que debera de pagar el alumno por la sancion
    def retrasos(self):
        if self.meses_retraso == 1:
            total_sancion = self.meses_retraso * self.sancion
            print(f"El libro lleva {self.meses_retraso} mes sin ser devuelto, debe pagar ${total_sancion}")
        elif self.meses_retraso == 2:
            total_sancion = self.meses_retraso * self.sancion
            print(f"El libro lleva {self.meses_retraso} meses sin ser devuelto, debe pagar ${total_sancion}")
        elif self.meses_retraso >= 3:
            print("Te has excedido en los meses de retraso, por lo tanto ya no podrás solicitar libros")
        else:
            print("El libro ha sido devuelto a tiempo. No hay sanción.")

#En esta funcion solamente hay inputs donde el usuario ingresara los datos
    def registro(self):
        self.alumno = input("Ingrese el nombre del alumno: ")
        self.codigo = input("Ingrese el código del estudiante: ")
        self.libro = input("Libro que se prestará: ")
        self.fecha = input("Ingrese la fecha en que se prestó el libro: ")
        self.carrera = input("Ingrese la carrera del alumno: ")
        self.fechaentrega = input("Ingrese la fecha de entrega: ")
        
 #Este input es clave ya que nos dice la cantidad de meses que usara la funcion anterior para sacar el monto de sancion a pagar       
        self.meses_retraso = int(input("Ingrese el número de meses de retraso: "))
#Por ultimo esta funcion es para la salida de los datos
    def mostrardato(self):
        print("--------------------------------------------")
        print("La lectura es importante")
        self.retrasos()
        print("--------------------------------------------")
        print(f"Alumno que prestó el libro: {self.alumno}")
        print(f"Código del alumno: {self.codigo}")
        print(f"Nombre del libro: {self.libro}")
        print(f"Fecha de préstamo: {self.fecha}")
        print(f"Fecha de entrega o habrá sanción: {self.fechaentrega}")


orden = Biblioteca()
orden.registro()  
orden.mostrardato()
