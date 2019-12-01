

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
        self.visited = [False] * (len(self.graph))
        self.setRootForSearch(root)

    def setRootForSearch(self,root):#pizzera
        node = [root,0,[]]# wierzchołek,odległość i trasa w postaci listy np[1,3,4,7,11]        czy odległość potrzebna?
        self.queue.append(node)
        self.visited[node[0] - 1] = True
       # print(self.queue)

    def bfsStep(self): #node jest postaći wierzchołek, "trasa"
        self.queue_one_iteration = self.queue.copy()
        #self.queue.clear()
        #print("\n qo11iter {}".format(self.queue_one_iteration))#add visited into consideration
        for node in self.queue_one_iteration:# dla wszystkich nodów w kolejce szukamy nowych nodów gdzie jeszcze nie byliśmy
            #print("bfs  :")
           # print(self.graph[node[0]])
            for nb in self.graph[node[0]]:
                if(self.visited[nb[0]-1]== False): #### IF FIRST VERTICSIS IS 0 CHANGE TO NB[0]
                    newNode = [nb[0],node[1]+nb[1],node[2]+[node[0]]]
                    self.queue.append(newNode)
                    self.visited[nb[0] - 1] = True
            #oznaczyć noda jako odwiedzonego i usunąć z kolejki

            self.queue.pop(0)
           # print("kolejka nowa: {}".format(self.queue))
          #  print(self.visited)

        return self.queue



class PierwszyNajtanszy:


    def __init__(self,graph,pizzeria,order):
        self.pizzeria = pizzeria
        self.order = order
        self.bfssearch = BFS(graph)

    def setPizzeria(self,pizzeria):
        self.pizzeria = pizzeria
    def setOrder(self,order):
        self.order = order
    def setGraph(self,graph):
        self.bfssearch = BFS(graph)

    def compareLists(self,queue,currentOrder):
        terminal_states = []
        for edge in currentOrder:
            for node in queue:
                if node[0] == edge[0] or node[0] == edge[1]: #   in
                     terminal_states.append(node)
        return terminal_states

    def searchForOnePath(self,root,currentOrder):
        self.bfssearch.reset(root)
        listOfFoundEdges = []# tak właściwie to lista z  wierzchołkami należącymi do krawędzi dostawy i odpowiednio trasami do nich
        while(listOfFoundEdges == []):
            self.bfssearch.bfsStep()
            listOfFoundEdges = self.compareLists(self.bfssearch.queue, currentOrder)
        return listOfFoundEdges

    def countDistance(self,listOfAllVisited):
        distance = 0
        for i in range(len(listOfAllVisited)-1):
            key =listOfAllVisited[i]
            for nb in self.bfssearch.graph[key]:
                if nb[0] == listOfAllVisited[i+1]:
                    distance+=nb[1]
                    break;
        return distance







    def planDelivery(self):
        root = self.pizzeria
        route = []
        while(self.order != []):
            possible_street_to_visit = self.searchForOnePath(root,self.order)
            if possible_street_to_visit == []:
                print("Fatal error:  part of edge doesnt exist")#mamy błąd bo krawedź nie isnieje
            else:
                node_of_street_to_visit = possible_street_to_visit.pop(0)
                for node in possible_street_to_visit:
                    if node[1] < node_of_street_to_visit[1]:
                        node_of_street_to_visit = node#wybraliyśmy do którego wierzchołka -> krawędzi idziemy

                vertex = node_of_street_to_visit[0]
                for edge in self.order:
                    if edge[0] == vertex:
                        root = edge[1]
                        self.order.remove([vertex, root])
                        break
                    elif edge [1] == vertex:
                        root = edge[0]
                        self.order.remove([root,vertex])
                        break

                route+= node_of_street_to_visit[2] + [node_of_street_to_visit[0]]

        nodePizzeria = self.searchForOnePath(root,[[self.pizzeria,self.pizzeria]])
        route += nodePizzeria[0][2] + [nodePizzeria[0][0]]
        return route









