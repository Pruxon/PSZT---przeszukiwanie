import graph_generator
from pathlib import Path

print("aaaaaa")
class1 = graph_generator.GraphCreator("graph.txt")
file_name = input("Enter file with graph:")



class1.ReadEdgesFromFile()
for x in class1.list1:
    print(x)
andy = class1.list1
class1.ConvertStringToNumber()
class1.CreateGraph()
print(class1.graph[2])