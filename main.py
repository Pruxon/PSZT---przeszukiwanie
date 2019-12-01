import ReadFromFileIntoGraph
import BFS
from pathlib import Path


class1 = ReadFromFileIntoGraph.GraphCreator("graph.txt")
#file_name = input("Enter file with graph:")
#class1.SetGraphName(file_name)


class1.readEdgesFromFile()
for x in class1.list1:
    print(x)
andy = class1.list1
class1.convertStringToNumber()
class1.createGraph()


order = ReadFromFileIntoGraph.readOrder("order.txt")
pizzeria = order.pop(0)[0]# now pizzeria has vertices(int ) and order has all the edges {list ot lists}

bfs1 = BFS.BFS(class1.graph)
bfs1.setRootForSearch(pizzeria)
bfs1.bfsStep(1)
bfs1.bfsStep(2)
bfs1.bfsStep(2)