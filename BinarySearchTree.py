
from Node import Node

#Clase
class BinarySearchTree:

    #Constructor donde se define a la variable de clase root como None
    def __init__(self):
        self.root = None

    def insert(self, label):
        # Creamos un nuevo nodo
        new_node = Node(label, None)
        # Si el árbol esta vacio el nodo de root es igual al nodo que ingresamos
        if self.empty():
            self.root = new_node
        else:
            # Si el árbol no esta vacio
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                #Se evalua si el valor ingresado es menor al nodo actual
                if new_node.getLabel() < curr_node.getLabel():
                    #si es menor al nodo actual extraemos el hijo de la izquierda del nodo actual
                    curr_node = curr_node.getLeft()
                else:
                    # si es mayor al nodo actual extraemos el hijo de la derecha del nodo actual
                    curr_node = curr_node.getRight()

            #se evalua si el valor del nodo es menor al nodo padre
            if new_node.getLabel() < parent_node.getLabel():
                #si es menor se asigna como hijo por la izquierda
                parent_node.setLeft(new_node)
            else:
                # si es mayor se asigna como hijo por la derecha
                parent_node.setRight(new_node)

            #asignamos el padre del nodo insertado
            new_node.setParent(parent_node)

    #Operación de borrado
    def delete(self, label):
        if (not self.empty()):
            node = self.getNode(label)
            if (node is not None):
                if (node.getLeft() is None and node.getRight() is None):
                    self.__reassignNodes(node, None)
                    node = None
                elif (node.getLeft() is None and node.getRight() is not None):
                    self.__reassignNodes(node, node.getRight())
                elif (node.getLeft() is not None and node.getRight() is None):
                    self.__reassignNodes(node, node.getLeft())
                else:
                    tmpNode = self.getMax(node.getLeft())
                    self.delete(tmpNode.getLabel())
                    node.setLabel(tmpNode.getLabel())

    def getNode(self, label):
        curr_node = None
        if (not self.empty()):
            curr_node = self.getRoot()
            while curr_node is not None and curr_node.getLabel() is not label:
                if label < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
        return curr_node


    def getMax(self, root=None):
        if (root is not None):
            curr_node = root
        else:
            curr_node = self.getRoot()
        if (not self.empty()):
            while (curr_node.getRight() is not None):
                curr_node = curr_node.getRight()
        return curr_node


    def getMin(self, root=None):
        if (root is not None):
            curr_node = root
        else:
            curr_node = self.getRoot()
        if (not self.empty()):
            curr_node = self.getRoot()
            while (curr_node.getLeft() is not None):
                curr_node = curr_node.getLeft()
        return curr_node


    def empty(self):
        if self.root is None:
            return True
        return False

    def __InOrderTraversal(self, curr_node):
        cadena = ""
        if (curr_node != None):
            #CONCATENAMOS LA PARTE IZQUIERDA DEL ARBOL
            cadena = cadena + self.__InOrderTraversal(curr_node.getLeft())
            #CONCATENAMOS EL VALOR DEL ROOT
            cadena = cadena + " " + str(curr_node.getLabel())
            #CONCATENAMOS LA PARTE DERECHA DEL ARBOL
            cadena = cadena + self.__InOrderTraversal(curr_node.getRight())
        return cadena

    def __InPreOrderTraversal(self, curr_node):
        cadena=""
        if (curr_node != None):
            #CONCATENAMOS EL VALOR DEL ROOT AL INICIO
            cadena = cadena + " " + str(curr_node.getLabel())
            # CONCATENAMOS LA PARTE IZQUIERDA DEL ARBOL
            cadena=cadena + self.__InPreOrderTraversal(curr_node.getLeft())
            # CONCATENAMOS LA PARTE DERECHA DEL ARBOL
            cadena=cadena +self.__InPreOrderTraversal(curr_node.getRight())
        return cadena


    def __InPostOrderTraversal(self, curr_node):
        cadena=""
        if (curr_node != None):
            # CONCATENAMOS LA PARTE IZQUIERDA DEL ARBOL
            cadena=cadena + self.__InPostOrderTraversal(curr_node.getLeft())
            # CONCATENAMOS LA PARTE DERECHA DEL ARBOL
            cadena=cadena +self.__InPostOrderTraversal(curr_node.getRight())
            # CONCATENAMOS EL VALOR DEL ROOT AL FINAL
            cadena = cadena +" " + str(curr_node.getLabel())
        return cadena



    def getRoot(self):
        return self.root


    def __isRightChildren(self, node):
        if (node == node.getParent().getRight()):
            return True
        return False


    def __reassignNodes(self, node, newChildren):
        if (newChildren is not None):
            newChildren.setParent(node.getParent())
        if (node.getParent() is not None):
            if (self.__isRightChildren(node)):
                node.getParent().setRight(newChildren)
            else:
                node.getParent().setLeft(newChildren)


    def traversalTree(self, traversalFunction=None, root=None):
        if (traversalFunction is None):
            return self.__InOrderTraversal(self.root)
        else:
            return traversalFunction(self.root)

    def printPreOrder(self):
        print("PREORDER >>", self.__InPreOrderTraversal(self.root))


    def printInOrder(self):
        print("INORDER >>" , self.__InOrderTraversal(self.root))


    def printPostOrder(self):
        print("POSTORDER >>" ,self.__InPostOrderTraversal(self.root))

    def printTree(self):
        print(">> ESTRUCTURA DEL ARBOL")
        self.__printTree(self.root,"")

    def sumaTree(self):
        print("SUMA DEL ARBOL>>",self.__sumaTree(self.root))

    def cantidadNodos(self):
        print("CANTIDAD DE NODOS DEL ARBOL>>",self.__cantidadNodos(self.root))

    # METODO PARA DIBUJAR EL ARBOL
    def __printTree(self, curr_node,prefijo):
        if (curr_node != None):
            #SE IMPRIME EL VALOR DEL NODO ACTUAL
            print(prefijo+" " +str(curr_node.getLabel()))
            #IMPRIMIR POR LA IZQUIERDA Y NOS INTRODUCIMOS CADA VEZ MAS
            self.__printTree(curr_node.getLeft() ,prefijo +"  ")
            #IMPRIMIR POR LA DERECHA Y NOS INTRODUCIMOS CADA VEZ MAS
            self.__printTree(curr_node.getRight() ,prefijo +"  ")

    # METODO PARA SUMAR  EL ARBOL
    def __sumaTree(self, curr_node):
        suma=0
        if (curr_node != None):
            # ACUMULAMOS EL VALOR DE LA VARIABLE SUMA CON EL VALOR DEL NODO
            suma= suma + curr_node.getLabel()
            #ACUMULAMOS EL VALOR DE LA VARIABLE SUMA POR LA IZQUIERDA
            suma= suma +self.__sumaTree(curr_node.getLeft())
            #ACUMULAMOS EL VALOR DE LA VARIABLE SUMA POR LA DERECHA
            suma= suma +self.__sumaTree(curr_node.getRight())
        return suma

    # METODO PARA SABER EL NIVEL
    def __cantidadNodos(self, curr_node):
        cantidad = 0
        if (curr_node != None):
            # ACUMULAMOS EL VALOR DE LA VARIABLE SUMA CON EL VALOR DEL NODO
            cantidad = cantidad + 1
            # ACUMULAMOS EL VALOR DE LA VARIABLE SUMA POR LA IZQUIERDA
            cantidad = cantidad + self.__cantidadNodos(curr_node.getLeft())
            # ACUMULAMOS EL VALOR DE LA VARIABLE SUMA POR LA DERECHA
            cantidad = cantidad + self.__cantidadNodos(curr_node.getRight())
        return cantidad




