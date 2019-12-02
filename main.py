import ReadFromFileIntoGraph
import BFS
import timeit

import time
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

start = timeit.default_timer()
#algorytm właściwy
route =finsearch.planDelivery()
stop = timeit.default_timer()


#wyświtlenie wyników
print(route)
distance =finsearch.countDistance(route)


print("Długość trasy w jednostkach umownych[j]:{}".format(distance))
print("Liczba przebytch krawędzi:{}".format(len(route)-1))
print("Czas wykonania [s]:{}".format(stop - start))
ReadFromFileIntoGraph.writeRouteToFile(route)
