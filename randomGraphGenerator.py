import random
MAX_DISTANCE = 20
MAX_NEIGHBOURS = 5
NUMBER_OF_VERTICLES = 10


class Graph:
    graph = {}
    list1 = []
    numberOfVerticles = NUMBER_OF_VERTICLES

    def __init__(self):
        self.graph = {
            1: self.list1
        }

    def initiateLists(self):
        for i in self.numberOfVerticles:
            list2 = []
            self.graph[i] = list2

    def initGraphGeneration(self):
        i = 0
        while i < self.numberOfVerticles:
            list2 = []
            distance = random.randint(1, MAX_DISTANCE)
            neighbour = ((i + 1) % self.numberOfVerticles, distance)
            self.graph[i] = list2
            if i == 1:
                self.graph[i].append(neighbour)
            else:
                list2.append(neighbour)
            i += 1

        i = 0
        while i < self.numberOfVerticles:
            if i == 0:
                distance = self.graph[NUMBER_OF_VERTICLES - 1][0][1]
                neighbour = [NUMBER_OF_VERTICLES - 1, distance]
            else:
                distance = self.graph[i - 1][0][1]
                neighbour = (i - 1, distance)
            self.graph[i].append(neighbour)
            i += 1

    def furtherGraphGeneration(self):
        for i in self.graph:
            alreadyConnected = len(self.graph[i])
            if alreadyConnected < MAX_NEIGHBOURS:
                neighboursNumber = random.randint(0, MAX_NEIGHBOURS - alreadyConnected)
                j = 0
                while j < neighboursNumber:
                    isRandomNumberIsNotConnected = 0
                    while isRandomNumberIsNotConnected < 1:
                        neighbourNumber = random.randint(1, NUMBER_OF_VERTICLES - 1)
                        if self.checkIfGeneratedVertexNumberIsCorrect(self, i, neighbourNumber):
                            isRandomNumberIsNotConnected = 1
                    distance = random.randint(1, MAX_DISTANCE)
                    pair1 = (i, distance)
                    pair2 = (neighbourNumber, distance)
                    self.graph[i].append(pair2)
                    self.graph[neighbourNumber].append(pair1)
                    j += 1

    def checkIfGeneratedVertexNumberIsCorrect(self, first, second):
        if first == second:
            return False
        if len(self.graph[second]) == MAX_NEIGHBOURS:
            return False
        alreadyConnected = len(self.graph[first])
        k = 0
        isOnTheList = 0
        while k < alreadyConnected:
            if second != self.graph[first][k][0]:
                isOnTheList += 1
            k += 1
        if isOnTheList != alreadyConnected:
            return False
        return True

    def saveToFile(self):
        with open("graph.txt", "w") as file:
            for i in self.graph:
                iStr = str(i)
                #file.write(iStr + ',')
                file.write('\n'.join(iStr +',' + ';'.join(str(x) for x in tu)for tu in self.graph[i]))
                file.write('\n')
