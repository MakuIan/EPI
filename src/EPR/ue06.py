'''
EPR 06 - Aufgabe 2
'''
__author__ = '8175858, Braun'
from graph import Graph


def get_graph():
    '''
    Takes in a graph in form of an adjacency list and returns it.
    '''
    graph_str = input('Please enter a graph in form of an adjacency list:')

    graph = Graph()
    vertex = ''
    for c in graph_str:
        if c == ':':
            print(c)
            prev = graph_str[graph_str.index(c) - 1]

            graph_str_list = list(graph_str)
            graph_str_list.remove(c)
            graph_str = ''.join(graph_str_list)

            vertex = prev

            graph.init_keys(vertex)
        elif c not in [' ', ':', ',', '[', ']', '{', '}']:
            graph.add(vertex, c)
    return graph


def is_tree(graph) -> bool:
    '''
    Takes in a graph and returns True if it is a tree, False otherwise.
    '''
    if any(value == [] for value in graph.items.values()):
        return False
    vertices = graph.get_num_vertices()
    edges = graph.get_num_edges()
    if edges != vertices - 1:
        return False
    if graph.is_cyclic():
        return False
    return True


if __name__ == '__main__':
    graph = get_graph()
    print(graph.items)
    print(is_tree(graph))
