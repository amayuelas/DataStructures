#!/usr/bin/env python
# -*- coding: latin-1 -*-
# LLenar con NIUs de los integrantes del grupo
# NIU_1: 1392631
# NIU_2: 1392661

from LinkedList import *

class Tree(object):
    """
    Class Tree
    """
    
    class Node(object):
        """
        Class Node
        """
        
        def __init__(self, data):
            """
            Builder of class Node, intializes each node with the parametre data
            and creates and empty list for childs
            :param data: what wants to be stored in the node
            """
            self.data = data
            self.childs = LinkedList()
            
        def addChild(self, child):
            """
            Adds node child to the list childs
            :param child: Node to be added
            """
            self.childs.insertAfter(child)
            
        def getChilds(self):
            """
            Returns the list of nodes childs
            :return : LinkedList of nodes childs         
            """
            return self.childs

        def getData(self):
            """
            Returns data of node
            :return : data of the node    
            """
            return self.data

        def getChild(self, data):
            """
            Searches child node that contains data and
            return this node or None if not found
            :param data: Data to search
            :return : the child (Tree.Node) or None if not found
            """

            aux = self.childs.head
            
            while aux != None:
                if aux.getData().getData() == data:
                    return aux.getData()
                else:
                    aux = aux.getNext()

            return None
                
        def __str__(self):
            """
            Creates string with the data of the node      
            :return : string with data of the node
            """
            return self.strRecursive('', True)
            
        def strRecursive(self, prefix, final):
            """
            Recurcive method that prints the node and all of its children
            :param prefix: string used for identation
            :param final: boolean for printing line to the children
            :return : string
            """            
            if final:
                contingut = prefix + '└── ' + str(self.data) + '\n'
                mascara =   prefix + '    '
            else:
                contingut = prefix + '├── ' + str(self.data) + '\n'
                mascara =   prefix + '│   '
            if self.childs.getSize() > 0:
                self.childs.moveHead()
                for idx in range(self.childs.getSize() - 1):
                    contingut += self.childs.getCurrent().strRecursive(mascara, False)
                    self.childs.moveNext()
                contingut += self.childs.getCurrent().strRecursive(mascara, True)
            return contingut

    def __init__(self):
        """
        Builder that initializes root variable
        """
        self.root = Tree.Node(None)

    def build(self, filename):
        """
        Reads data from disk and saves it in the tree by using function add
        :param filename: Filename from which it takes the input
        """
        f = open(filename, 'r')
        for linia in filter(lambda x: len(x.split()) == 18, f.readlines()):
            self.add(linia.split())
        f.close()

        
    def add(self, features):
        """
        Adds data from list features
        param features: list to be added
        """
        i = 0
        current = self.root
        next = self.root.getChild(features[i])
        while next != None:
            current = next
            i += 1
            next = current.getChild(features[i])

        for i in range(i, len(features)):
            new = Tree.Node(features[i])
            current.addChild(new)
            current = new

        

   
    def search(self, features):
        """
        Gets through the vector features and returns the data from the leaf, 
        in case it doesn't get there, returns IndexError
        :param features: List which contains the path to be searched
        :return : Index Error if the path doesn't exist; 
        """
        current = self.root
        for element in features:
            current = current.getChild(element)
            if current == None:
                raise IndexError
        children = current.getChilds()
        return children.getHead().getData()
            
        
    def __str__(self):
        """
        Returns an ascii multiline representation of the tree
        :param features: Agregar comentarios
        :return : Agregar comentarios
        """        
        contingut = 'ROOT\n'
        if self.root.getChilds().size() > 0:
            self.root.getChilds().moveHead()
            for idx in range(self.root.getChilds().size() - 1):
                contingut += self.root.getChilds().getCurrent().strRecursive('', False)
                self.root.getChilds().moveNext()
            contingut += self.root.getChilds().getCurrent().strRecursive('', True)
        return contingut 


if __name__ == '__main__':
    """
    Sample usage of class Tree.
    """
    t = Tree()
    print "Creant l'arbre"
    t.build('contrasenyes.txt')
    f = open('contrasenyes.txt', 'r')
    dades = filter(lambda x: len(x.split()) == 18, f.readlines())
    f.close()
    for consulta in dades:
        consulta = consulta.split()
        caracteristiques = consulta[:-1]
        animal = consulta[-1]
        resultat = t.search(caracteristiques)
        print "Comprovant %s" % animal
        if animal != resultat:
            raise ValueError, "S'esperava %s però s'ha trobat %s" % (animal, resultat)
    print "ok"
    print t
