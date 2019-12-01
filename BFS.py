

class BFS:
    queue = []
    queue_one_iteration = []# pomocnicza koleja dla jednago kroku,który się wykonuje dla wszystkich znalezionych wierzchołków w poprzedniej iteracji
    visited = []# odwiedzone
    graph = {}


    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * (len(self.graph))
    def assingGraph(self,graph):
        self.graph = graph

    def reset(self,root):# resetujemy dane o krokach
        self.queue.clear()
        self.queue_one_iteration.clear()
        self.visited.clear()
        self.setRootForSearch()

    def setRootForSearch(self,pizzeria):#pizzera
        node = [pizzeria,0,[]]# wierzchołek,odległość i trasa w postaci listy np[1,3,4,7,11]        czy odległość potrzebna?
        self.queue.append(node)
        self.visited[node[0] - 1] = True
        print(self.queue)

    def bfsStep(self,terminal_states): #node jest postaći wierzchołek, "trasa"
        self.queue_one_iteration = self.queue.copy()
        #self.queue.clear()
        print("\n qo11iter {}".format(self.queue_one_iteration))#add visited into consideration
        for node in self.queue_one_iteration:# dla wszystkich nodów w kolejce szukamy nowych nodów gdzie jeszcze nie byliśmy
            print("bfs  :")
            print(self.graph[node[0]])
            for nb in self.graph[node[0]]:
                if(self.visited[nb[0]-1]== False): #### IF FIRST VERTICSIS IS 0 CHANGE TO NB[0]
                    newNode = [nb[0],node[1]+nb[1],node[2]+[node[0]]]
                    self.queue.append(newNode)
                    self.visited[nb[0] - 1] = True
            #oznaczyć noda jako odwiedzonego i usunąć z kolejki

            self.queue.pop(0)
            print("kolejka nowa: {}".format(self.queue))
            print(self.visited)

        return self.queue



