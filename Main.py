"""
PROPUESTA DE PROTIPO DE BUSQUEDA UTILIZANDO EL ALGORITMO B-TREE

------------------------------
Integrantes
------------------------------
Aimituma Diaz, Jose Luis
Aisa Incapuño, Sixto Santiago
Marca Perez, Jhon Elvis
Rodríguez Herrera, Eduardo
Taco Torres, Ayrton Renato
Venegas Vasquez, Nikols Dery


"""
#IMPORTAMOS LA CLASES
from BinarySearchTree import BinarySearchTree
from Menu import Menu

#INSTANCIAMOS LA CLASE MENU
menu = Menu()
arbol=BinarySearchTree()
while True:
    # Dibujamos el Menu Principal
    menu.print_Menu()
    # Capturamos la opción seleccionada por el usuario
    opcionMenu = menu.get_Option()

    if (opcionMenu == "1"):
        menu.print_Title("INGRESO DE ELEMENTOS EN EL ARBOL")
        elemento = int(input("\tIngrese el Elemento : "))
        arbol.insert(elemento)
        print(">> Se agrego el elemento al arbol")

        arbol.printTree()
        arbol.cantidadNodos()
        arbol.sumaTree()

    elif (opcionMenu == "2"):
        menu.print_Title("ELIMINAR ELEMENTOS DEL ARBOL")
        valorIngresado = int(input("\tIngrese el Elemento a eliminar : "))
        elementoBuscado=arbol.getNode(valorIngresado)

        if (elementoBuscado == None):
            print(">> El elemento ingresado no existe")
        else:
            arbol.delete(valorIngresado)

            print(">> Se elimino el elemento del arbol ")
        arbol.printTree()
        arbol.cantidadNodos()
        arbol.sumaTree()
    elif (opcionMenu == "3"):
        menu.print_Title("BUSCANDO ELEMENTO DEL ARBOL")

        valorIngresado = int(input("\tIngrese el Elemento a buscar : "))
        elementoBuscado = arbol.getNode(valorIngresado)

        if (elementoBuscado == None):
            print(">> El elemento ingresado no existe")
        else:
            print(">> El elemento econtrado ")

    elif (opcionMenu == "4"):
        menu.print_Title("ELEMENTOS ACTUALES")
        arbol.printTree()
        arbol.cantidadNodos()

    else:
        menu.print_Error()
    # Indicamos al usuario que presione una tecla para continuar
    menu.print_Continue()
