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
list_1+=[2,3]
print(list_1 )
list_1+=[4,5]
print(list_1 )



