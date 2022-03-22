#@EricP 2022
import numpy as np

class WidthCourse:
    """This Class give the width course of a matrice """
    def __init__(self, matrice, index):
        self.matrice = np.array(matrice)
        self.index = int(index)
        self.file = [index]
        self.length = len(matrice)
        self.path = []
        self.colors = self.buildEmptySet()
        self.main()

    def buildEmptySet(self) -> list:
        """ Build an array of int 999 to use as ''Blank'' element """
        myArray = []
        for i in range(self.length):
            myArray.append(999)
            
        myArray[self.index] = True
        return myArray
    
    def fillPath(self):
        """ Fill the Path Array with all the road taken """
        for i in range(len(self.colors)):
            if self.colors[i] == False:
                if not i in self.path:
                    self.path.append(i)

    def editNewColors(self, indexes):
        """ Changes the specific element given by the indexes """
        for i in range(len(indexes)):
            if self.colors[indexes[i]] == 999:
                self.colors[indexes[i]] = True

    def getLinkedSommets(self, sommet) -> list:
        myRange  = self.matrice[sommet]
        myArray = []
        for i in range(len(myRange)):
            if myRange[i] == 1:
                myArray.append(i)
        return myArray

    def removeElement(self, array, element):
        """ Remove aa given element from the given array """
        for i in range(len(array)):
            if element == array[i - 1]:
                array.pop(i - 1)

    def allGreen(self, array) -> bool:
        """ Return True if all the element from the given array are True """
        balise = True
        for i in array:
            if i != True:
                balise = False
                break
        return balise

    def iteration(self) -> list:
        """ The main loop of the class """
        # Get array of all the sommets linked to to targeted one
        sommetsLinked = self.getLinkedSommets(self.index)
        # Linked AND green (White) ones 
        validElement = []
        for i in sommetsLinked:
            if self.colors[i] == 999:
                validElement = validElement + [i]
        # Concatenate the current file with the new valid Element
        self.file = self.file + validElement
        # Edit the Colors Array putting them in green (True)
        self.editNewColors(validElement)
        # Current index put in RED (False)
        self.colors[self.index] = False

        # Removing RED (False) element from the file
        for i in range(len(self.colors)):
            if self.colors[i] == False:
                if i in self.file:
                    self.file.remove(i)

        self.fillPath()

        if (len(self.file) > 0): 
            self.index = self.file[0]

    def main(self) -> list:
        """ Launcher of the class functions """
        while len(self.file) != 0:
            self.iteration()
        return self.path

    def getPath(self) -> list:
        return self.path

    def getColor(self) -> list:
        return self.colors


myGraph = np.array([
    #A  B  C  D  E  F  G
    [0, 0, 1, 1, 0, 0, 0], #A
    [1, 0, 0, 0, 1, 0, 0], #B
    [0, 1, 0, 1, 0, 0, 0], #C
    [0, 0, 0, 0, 1, 0, 1], #D
    [0, 0, 0, 0, 0, 1, 0], #E
    [0, 0, 0, 0, 1, 0, 0], #F
    [0, 1, 0, 0, 0, 0, 0]  #G
    ])

myCourse = WidthCourse(myGraph, 0)
print(myCourse.getPath())
