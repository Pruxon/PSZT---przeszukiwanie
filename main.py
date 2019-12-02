import ReadFromFileIntoGraph
import BFS
from pathlib import Path
DEFAULT_NAME = "graph.txt"

#instalowanie grafu
RFF = ReadFromFileIntoGraph.GraphCreator(DEFAULT_NAME)
file_name = input("Enter file with graph:")
RFF.setGraphName(file_name)
RFF.readEdgesFromFile()
RFF.convertStringToNumber()
RFF.createGraph()

#instalacja zamówienia
orderfile = input("Enter order file:")
order = ReadFromFileIntoGraph.readOrder(orderfile)
pizzeria = order.pop(0)[0]

#inicjalizacja klasy obługującej algorytm
finsearch = BFS.PierwszyNajtanszy(RFF.graph,pizzeria,order)

#algorytm właściwy
route =finsearch.planDelivery()

#wyświtlenie wyników
print(route)
distance =finsearch.countDistance(route)
print(distance)
