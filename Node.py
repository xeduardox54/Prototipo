# Declaramos la clase "Node"
class Node:
    #CONSTRUCTOR
    def __init__(self, label, parent):
        self.label = label#VALOR DEL NODO
        self.left = None#HIJO IZQUIERDO
        self.right = None#HIJO DERECHO
        self.parent = parent#PADRE DEL NODO

    #METODOS GETTER Y SETTER
    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent
