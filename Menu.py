import os
#Definimos la clase Menu
class Menu():
    def limpiar(self):
        os.system('cls')

    def print_Menu(self):
        self.limpiar()
        self.print_Title("PROTOTIPO INCREMENTAL PARA BUSQUEDA DE INFORMACIÓN")

        print("\t1 - AGREGAR ELEMENTOS")
        print("\t2 - ELIMINAR ELEMENTOS")
        print("\t--------------------------")
        print("\t3 - BUSCAR ELEMENTO")
        print("\t--------------------------")
        print("\t4 - MOSTRAR ELEMENTOS")
        print("\t--------------------------")
        print("\t0 - EXIT")

    def print_Title(self,title):
        self.limpiar()
        print("-----------------------------")
        print("  " + title+ "  ")
        print("-----------------------------")

    def get_Option(self):
        opcionMenu = input("Seleccione una opcion del Menú Principal : ")
        return opcionMenu

    def print_Error(self):
        print("-----------------------------------")
        print("Ha seleccionado una opción invalida")
        print("Intente de nuevo")
        print("-----------------------------------")
 
    def print_Continue(self):
        print("-----------------------------------")
        input("Presione una tecla para continuar")

    def print_Mensaje(self):
        print(">> Operación realizada con ¡ Exito ! <<")
