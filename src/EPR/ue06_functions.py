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

    graph.items = eval(graph_str)
    if not isinstance(graph.items, dict):
        raise TypeError
    return graph


def is_tree(graph) -> bool:
    '''
    Takes in a graph and returns True if it is a tree, False otherwise.
    '''
    # if any(value == [] for value in graph.items.values()):
    #     return False
    vertices = graph.get_num_vertices()
    edges = graph.get_num_edges()
    # if edges != vertices - 1:
    #     return False
    return graph.isCyclic()


if __name__ == '__main__':
    try:
        graph = get_graph()
        print(graph.items)
        print(is_tree(graph))
        print(graph.convert_to_undirected())
    except TypeError as e:
        print('Please enter a valid graph.')
        print(e)
