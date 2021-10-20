import pygame
import bfs
from random import randint


class Node:

    def __init__(self, coords, number):
        self.number = number
        self.coords = coords


def create_node_circle(window, occurred_spots, nodeNumber):


    node_current_occurrence_coords = (randint(200, 1500), randint(10, 600))

    pygame.font.init()
    nodeFont = pygame.font.SysFont('Comic Sans MS', 19)


    if node_current_occurrence_coords not in occurred_spots:
        occurred_spots.append(node_current_occurrence_coords)
        pygame.draw.circle(window, (255, 255, 0),
                           node_current_occurrence_coords, 20)
        textsurface = nodeFont.render(f"{nodeNumber}", False, (255, 0, 255))
        window.blit(textsurface, (node_current_occurrence_coords[0] - 9, node_current_occurrence_coords[1] - 15))

    else:
        create_node_circle(window, occurred_spots, nodeNumber)

    return node_current_occurrence_coords


def init_graph(graph, node_list, window, occurred_spots):

    for i in range(graph.shape[0]):
        node_list.append(Node(create_node_circle(window, occurred_spots, i), i))

    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            if graph[i][j] > 0:
                pygame.draw.line(window, (255, 255, 255),
                                 node_list[i].coords, node_list[j].coords, 2)

    
    pygame.font.init()
    nodeFont = pygame.font.SysFont('Comic Sans MS', 19)

    for i in range(graph.shape[0]):
        pygame.draw.circle(window, (255, 255, 0), node_list[i].coords, 20)
        textsurface = nodeFont.render(f"{node_list[i].number}", False, (255, 0, 255))
        window.blit(textsurface, (node_list[i].coords[0] - 9, node_list[i].coords[1] - 15))


def returnNodeIndices(node):
    x = node.split(',')
    return x[0], x[1]


def trackDiscoveredNodes(window, discovered_nodes_render, node_list, graph):

    for i in range(0, len(discovered_nodes_render), 2):
        pygame.draw.circle(window, (0, 0, 255),
                           discovered_nodes_render[i].coords, 20)

        try:
            pygame.draw.line(window, (255, 0, 0), discovered_nodes_render[i].coords, discovered_nodes_render[i+1].coords, 2)
        except:
            pass

    pygame.font.init()
    nodeFont = pygame.font.SysFont('Comic Sans MS', 19)

    for i in range(graph.shape[0]):
        pygame.draw.circle(window, (255, 255, 0), node_list[i].coords, 20)
        textsurface = nodeFont.render(f"{node_list[i].number}", False, (255, 0, 255))
        window.blit(textsurface, (node_list[i].coords[0] - 9, node_list[i].coords[1] - 15))

    


def main():

    graph = bfs.np.array([[0, 3, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [3, 0, 5, 2, 5, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [4, 5, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 2, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    [2, 5, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
    [0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

    # graph = bfs.np.array([[0, 0, 0, 1, 2], 
    #                 [0, 0, 1, 3, 3], 
    #                 [0, 1, 0, 6, 0], 
    #                 [1, 3, 6, 0, 0], 
    #                 [2, 3, 0, 0, 0]])

    discovered = {}
    tree = []

    tree = bfs.bfs(graph, tree, discovered)

    # print(tree)

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

        if init_flag == 0:
            init_graph(graph, node_list, window, occurred_spots)
            init_flag = 1

        try:
            node = tree.pop(0)
        except IndexError:
            print("Breadth First Search Complete ")
            run = False
            exit(0)

        i, j = returnNodeIndices(node)

        discovered_nodes_render.append(node_list[int(i)])
        discovered_nodes_render.append(node_list[int(j)])
        trackDiscoveredNodes(window, discovered_nodes_render, node_list, graph)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

    
        pygame.display.update()

        pygame.time.wait(1000)

    pygame.quit()


if __name__ == '__main__':
    main()
