import ReadFromFileIntoGraph
import BFS
import randomGraphGenerator
from pathlib import Path

print("aaaaaa")
class1 = readFromFileToGraph.GraphCreator("graph.txt")
file_name = input("Enter file with graph:")

class1 = ReadFromFileIntoGraph.GraphCreator("graph.txt")
#file_name = input("Enter file with graph:")
#class1.SetGraphName(file_name)


class1.readEdgesFromFile()

class1.convertStringToNumber()
class1.createGraph()


order = ReadFromFileIntoGraph.readOrder("order.txt")
pizzeria = order.pop(0)[0]# now pizzeria has vertices(int ) and order has all the edges {list ot lists}
finsearch = BFS.PierwszyNajtanszy(class1.graph,pizzeria,order)

route =finsearch.planDelivery()
print(route)
distance =finsearch.countDistance(route)
print(distance)
#print(finsearch.searchForOnePath(pizzeria,order))