import random
MAX_DISTANCE = 20
MAX_NEIGHBOURS = 5
NUMBER_OF_VERTICLES = 10000
MAX_ORDERS = 100

class RandomGraph:
    graph = {}
    list1 = []
    orders = []
    pizzeria = 0
    numberOfVerticles = NUMBER_OF_VERTICLES

    def __init__(self):
        self.graph = {
            1: self.list1
        }
        pizzeria = random.randint(0, self.numberOfVerticles-1)

    def initiateLists(self):
        for i in self.numberOfVerticles:
            list2 = []
            self.graph[i] = list2

    def initGraphGeneration(self):
        self.pizzeria = random.randint(0, self.numberOfVerticles-1)
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
                file.write('\n'.join(iStr + ',' + ';'.join(str(x) for x in tu)for tu in self.graph[i]))
                file.write('\n')

    def generateTaskList(self):
        temp = self.graph
        numberOfEdges = 0
        vertexCheck = 0
        for i in self.graph:
            numberOfEdges += len(self.graph[i])
        #numberOfOrders = random.randint(1, MAX_ORDERS)
        numberOfOrders = MAX_ORDERS
        for i in range(numberOfOrders):
            randomVertex = 0
            vertexCheck = 0
            while vertexCheck < 1:
                randomVertex = random.randint(0, NUMBER_OF_VERTICLES - 1)
                if len(temp[randomVertex]) != 0:
                    vertexCheck = 1
            listLenght = len(temp[randomVertex])
            if listLenght != 1:
                randomElement = random.randint(0, listLenght - 1)
            else:
                randomElement = 0
            anotherVertex = temp[randomVertex][randomElement][0]
            self.orders.append((randomVertex, anotherVertex))
            counter = 0
            while counter < len(temp[anotherVertex]):
                if temp[anotherVertex][counter][0] != randomVertex:
                    counter += 1
                else:
                    break
            del(temp[randomVertex][randomElement])
            del(temp[anotherVertex][counter])

        for i in range(0, NUMBER_OF_VERTICLES-1):
            print(temp[i])

    def ordersToFile(self):
        with open("order.txt", "w") as file:
            file.write(str(self.pizzeria))
            file.write('\n')
            file.write('\n'.join(','.join(str(x) for x in tu)for tu in self.orders))


graph = RandomGraph
graph.initGraphGeneration(graph)
graph.furtherGraphGeneration(graph)
graph.generateTaskList(graph)
graph.saveToFile(graph)
graph.ordersToFile(graph)