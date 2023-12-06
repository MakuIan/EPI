'''
EPR 06 - Aufgabe 2
'''
__author__ = '8175858, Braun'
from graph import Graph
import ast


def get_graph():
    '''
    Takes in a graph in form of an adjacency list and returns it.
    '''
    graph_str = input('Please enter a graph in form of an adjacency list:')

    graph = Graph()
    try:
        graph.items = ast.literal_eval(graph_str)
        if not isinstance(graph.items, dict):
            print('Invalid input.')
            return get_graph()
    except (SyntaxError, TypeError):
        print('Invalid input.')
        return get_graph()
    return graph


def is_tree(graph) -> bool:
    '''
    Takes in a graph and returns True if it is a tree, False otherwise.
    '''
    for vertice in graph.items.keys():
        if graph.is_vertex_isolated(vertice):
            return False
    ugraph = graph.convert_to_undirected()
    vertices = len(ugraph.keys())
    print('ugraph:', ugraph)
    edges = sum(len(edges) for edges in ugraph.values()) // 2
    if edges != vertices - 1:
        return False
    return graph.isCyclic()


if __name__ == '__main__':
    graph = get_graph()
    print(graph.items)
    print(graph.convert_to_undirected())
    print(is_tree(graph))
