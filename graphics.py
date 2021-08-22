import pygame
import bfs
from random import randint
from time import sleep

class Node:

    def __init__(self, coords, number):
        self.number = number
        self.coords = coords



def create_node_circle(window, occurred_spots):

    node_current_occurrence_coords = (randint(200, 1500), randint(10, 600))
   
    if node_current_occurrence_coords not in occurred_spots:
        occurred_spots.append(node_current_occurrence_coords)
        pygame.draw.circle(window, (255, 255, 0), node_current_occurrence_coords, 10)

    else:
        create_node_circle(window, occurred_spots)
        
    return node_current_occurrence_coords



def init_graph(graph, node_list, window, occurred_spots):

    for i in range(graph.shape[0]):
        node_list.append(Node(create_node_circle(window, occurred_spots), i))
    
    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            if graph[i][j] > 0:
                pygame.draw.line(window, (255, 255, 255), node_list[i].coords, node_list[j].coords, 2)


def returnNodeIndices(node):
    x = node.split(',')
    return x[0], x[1]


def trackDiscoveredNodes(window, discovered_nodes_render):

    for i in range(len(discovered_nodes_render)):
        pygame.draw.circle(window, (0, 0, 255), discovered_nodes_render[i].coords, 10)

        i += 1

def main():

   #  graph = bfs.np.array([[1,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0],
   #      [0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1],
   #      [1,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0],
   #      [0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0],
   #      [1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0],
   #      [0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0],
   #      [1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,0],
   #      [0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1],
   #      [1,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1],
   #      [0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1],
   #      [0,0,1,1,1,0,1,1,1,1,0,0,1,0,1,0],
   #      [1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,0],
   #      [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0],
   #      [1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,1],
   #      [0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0],
   #      [0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,1]])

    graph = bfs.np.array([[0, 0, 1, 1, 0, 0], 
          [0, 0, 0, 1, 1, 1], 
          [1, 0, 0, 0, 1, 0], 
          [1, 1, 0, 0, 0, 0], 
          [0, 1, 1, 0, 0, 1], 
          [0, 1, 0, 0, 1, 0]])

    discovered = {}
    tree = []

    tree = bfs.bfs(graph, tree, discovered)
    
    pygame.init()
    window_height = 700
    window_width = 1800
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pygame Testing")

    run = True

    occurred_spots = []
    node_list = []

    init_flag = 0


    discovered_nodes_render = []

    while run:

        sleep(5)

        if init_flag is 0:
            init_graph(graph, node_list, window, occurred_spots) 
            init_flag = 1 

        try:
            node = tree.pop(0)
        except IndexError:
            print("Breadth First Search Complete ")
            run = False

        i, j = returnNodeIndices(node)

        discovered_nodes_render.append(node_list[int(i)])
        discovered_nodes_render.append(node_list[int(j)])
        trackDiscoveredNodes(window, discovered_nodes_render)
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
         
        pygame.display.update()
        
    pygame.quit()



if __name__ == '__main__':
    main()

