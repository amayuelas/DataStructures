class LinkedList(object):
    class Node(object):
        """ Esta clase guarda los elementos de la lista en nodos"""
        
        def __init__(self, data, siguiente = None):
            """ Incializa el nodo con data y la referencia al nodo siguiente (por defecto None)
                Parametros:
                data
                next
                """
            
            self.__data = data
            self.__next = siguiente
            
        def getData(self):
            """ Retorna el contenido del nodo """
            return self.__data
            
        def getNext(self):
            """ Retorna el nodo siguiente """
            return self.__next
            
        def setData(self, data):
            """ Rellena el nodo con la informacion que se pasa por parametro
                data: Contenido del nodo que se quiere guardar
                """
            self.__data = data
            
        def setNext(self, siguiente):
            """ Se enlaza el siguiente nodo
                next: Nodo que se quiere enlazar
                """
            self.__next = siguiente
            
        def __str__(self):
            """ Metodo para configurar la funcion print del nodo """
            return str(data)

    def __init__(self):
        """ Inicializa la lista como una lista vacia """
        self.__current = Node()
        self.__head = Node()
        self.__tail = Node()
        self.__size = 0

    def getHead(self):
        """ Retorna los datos guardados en el primer nodo de la lista """
        
        if self.isEmpty(): raise IndexError, "La lista esta vacia"
        return self.__head.getData()
        
    def getTail(self):
        """ Retorna los datos guardados en el ultimo nodo de la lista """
        
        if self.isEmpty():
            raise IndexError, "La lista esta vacia"
        return self.__tail.getData()
        
    def getCurrent(self):
        """ Retorna los datos guardados en el nodo actual """
        
        if self.isEmpty(): raise IndexError, "La lista esta vacia"
        return self.__current.getData()
        
    def moveNext(self):
        """ Mueve __current al siguiende nodo de la lista """
        
        if self.isEmpty(): raise "La lista esta vacia"
        if self.__curent == self.__tail : raise "Current apunta al ultimo elemento"
        
        self.__current = self.__current.getNext()
        
    def moveHead(self):
        """ Mueve __current al primer nodo de la lista """
        
        if self.isEmpty(): raise IndexError, "La lista esta vacia"
        self.__current = self.__head
        
    def isEmpty(self):
        """ Comprueba si la lista esta vacia y retorna si True si lo esta """
        return self.__head == None
        
    def getSize(self):
        """ Retorna el numero de elementos de la lista """
        return self.__size
    
    def clear(self):
        self.__head = None
        self.__tail = None
        
        
    def insertBefore(self, data):
        """ Agrega el data un antes del que senala el current """
        
        new = Node()
        if self.isEmpty():
            self.__head = new
            self.__tail = new
            self.__current = new
        elif self.__current == self__head:
            new.setNext(self.__head)
            self.__head = new
            self.__current = new
        else:
            aux = self.__head
            while aux.getNext() != self.__current:
                aux.setNext(aux.getNext())
            new.setNext(aux.getNext())
            aux.setNext(new)

        self.__size += 1
           
            
    def insertAfter(self, data):
        """Anade el data uno después del que señala el current """
        
        new = Node(data)
        if self.isEmpty():
            self.__head = new
            self.__tail = new
            self.__current = new
            
            
        elif self.__current == self.__tail:
            self.__current.setNext(new)
            self.__tail = new
            self.__current = self.__tail
            
        else:
            new.setNext(self.__current.setNext())
            self.__current.setNext(new)
            self.__current = new
            
        self.__size += 1
        
    def remove(self):
        """ Borra el nodo actual, decremente __size en 1 y mueve current al nodo anterior si posible"""
        
        if self.isEmpty(): raise IndexError, "La lista esta vacia"
        if self.getSize() == 1:
            self.__current.remove()
            self.__head = None
            self.__tail = None
            self.__current = None
        elif self.__current == self.__tail:
            self.__current.remove()
            aux = self.__head
            while aux.getNext() != None:
                aux.setNext(aux.getNext())
            self.__tail = aux
            self.__current = aux
        else:
            aux = self.__head
            while aux.getNext() != self.__current:
                aux.setNext(aux.getNext())
            aux.setNext(self.__current.getNext())
            self.__current.remove()

        self.__size -= 1
        
    def __str__(self):
        """ Metodo para configurar la funcion print de la lista """
        
        aux = Node(self.__head)
        
        while (aux != self.__tail):
            print(aux.__str__())
            aux = aux.getNext()
        
