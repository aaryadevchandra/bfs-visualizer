import numpy as np
from time import sleep

class Node:

    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val
        self.indexcomb = str(i) + str(j)


class Edge:

    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.edgecomb = str(u) + "," + str(v)

def displayNodeGraph(node_graph):

    for i in range(len(node_graph)):
        for j in range(len(node_graph)):
            print(node_graph[i][j].val) 

def checkTreeAddingCondition(tree, edge):

    if (str(edge.v) + str(edge.u)) in tree:
        return -1
    else:
        return 1

def bfs(graph, tree, discovered):

    node_graph = []

    # converting the 2-D numpy matrix to a 2-D list of type 'Node'
    for i in range(graph.shape[0]):
        graph_row = []
        for j in range(graph.shape[1]):
            node = Node(i, j, graph[i, j])
            graph_row.append(node)

        node_graph.append(graph_row)

    # setting all discovered to false
    discovered[node_graph[0][0].indexcomb] = True
    for i in range(len(node_graph)):
        for j in range(len(node_graph[0])):
            if i != 0 or j != 0:
                discovered[node_graph[i][j].indexcomb] = False

    L = []
    L.append(node_graph[0][0]) 

    while len(L) != 0: 
        curr_node = L.pop(0)
        for j in range(len(node_graph[curr_node.i])):
            if node_graph[curr_node.i][j].val > 0 and discovered[node_graph[curr_node.i][j].indexcomb] == False:
                discovered[node_graph[curr_node.i][j].indexcomb] = True
                edge = Edge(curr_node.i, j)
                if checkTreeAddingCondition(tree, edge) == 1:
                    tree.append(edge.edgecomb) 
               # print(tree)
               # print('\n\n')
                L.append(node_graph[j][curr_node.i])
    
    return tree
   

# def main():

   #  graph = np.array([[0, 0, 3, 0, 0, 5, 0],
   #      [0, 0, 0, 0, 11, 7, 18], 
   #      [3, 0, 0, 0, 0, 0, 11], 
   #      [0, 0, 0, 0, 8, 0, 3], 
   #      [0, 11, 0, 8, 0, 1, 0], 
   #      [5, 7, 0, 0, 1, 0, 0], 
   #      [0, 18, 11, 3, 0, 0, 0]])


    # graph = np.array([[1,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0],
    #     [0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1],
    #     [1,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0],
    #     [0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0],
    #     [1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0],
    #     [0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0],
    #     [1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,0],
    #     [0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1],
    #     [1,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1],
    #     [0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1],
    #     [0,0,1,1,1,0,1,1,1,1,0,0,1,0,1,0],
    #     [1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,0],
    #     [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0],
    #     [1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,1],
    #     [0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0],
    #     [0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,1]])

   #  discovered = {}
   #  tree = []

   #  tree =  bfs(graph, tree, discovered)
   #  print(tree)



# if __name__ == '__main__':
#     main()
