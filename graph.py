# opening text graph and then creating the structure  //class not yet implemented
import re 

#graph_file_name = input("graph name: ")
graph_file_name = "graph.txt"

print(graph_file_name)

try:
    file = open(graph_file_name,"rt")
except IOError:
    print("loading graph failure")


list_1 = []
#for x in file:
    #print(x)
 #   list_1.append(x)



d1 ={}
d1.update({1:2})
d1.update({2:[3]})
d1.update({2:d1.get(2)+[[8],[9]]})
print(d1)


