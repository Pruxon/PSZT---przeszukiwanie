#class that loads egdes from text file and generates graph
import re

# dictionary of lists of sets     set(vertices,distance)
class GraphCreator:
    list1 = []
    graph = {}
    list2 = []
    def __init__(self,file_name):
        self.name = file_name

    def setGraphName(self,file_name):
        self.name = file_name

    def getGraph(self):
        return self.graph

    def readEdgesFromFile(self):

        try:
            file = open(self.name, "rt")
        except IOError:
            print("loading graph failure")

        for line in file:
            self.list1.append(line)
        file.close()
        print( self.list1)

    def convertStringToNumber(self):

        for line in self.list1:

            self.list2.append([int(s) for s in re.findall(r'\b\d+\b',line)])#check correctness of this line
        print(self.list2)

    def createGraph(self):

        for edge in self.list2:
            neighbour = (edge[1],edge[2])# tuple consisting the neighbour of
            if edge[0] in self.graph:
                 self.graph[edge[0]].append(neighbour)
            else:
                self.graph[edge[0]] =[neighbour]
             #same operation for second vertices in the edge
            neighbour = (edge[0],edge[2])

            if edge[1] in self.graph:
                 self.graph[edge[1]].append(neighbour)
            else:
                self.graph[edge[1]] = [neighbour]



        print(self.graph)
                            # file must be of format 2 edges in each line
def readOrder(file_name):#fucntion that takes file name as an arugment and returns list of edges(sets)
    with open(file_name)as file:
        list1 = []
        for line in file:
            list1.append(line)
        listOrder = []
        for line in list1:
            listOrder.append([int(s) for s in re.findall(r'\b\d+\b',line)])
        return listOrder


