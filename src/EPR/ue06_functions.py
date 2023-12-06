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
    print(graph.items)
    vertices = len(ugraph.keys())
    print('ugraph:', ugraph)
    edges = sum(len(edges) for edges in ugraph.values()) // 2
    if edges != vertices - 1:
        return False
    return graph.isCyclic()


def get_leafs(graph):
    '''
    Takes in a graph and returns a set of leafs.
    '''
    leafs = set()
    for vertex, edges in graph.items.items():
        print(len(edges))
        if (len(edges) == 0):
            leafs.add(vertex)
    return leafs


def has_root(graph):
    '''
    Takes in a graph and returns True if it has a root, False otherwise.
    '''
    in_degree_counter = {vertex: 0 for vertex in graph}
    for vertex, edges in graph.items():
        for edge in edges:
            in_degree_counter[edge] += 1

    root_found = False
    found_vertex = None
    for vertex in graph:
        if in_degree_counter[vertex] == 0:
            if root_found:
                return False, None  # more than one root
            root_found = True
            found_vertex = vertex
    return root_found, found_vertex


# {0: [1, 2], 1: [], 2: []}
# {0:[1,2],1:[],2:[],3:[2]}
# {'A': ['B'], 'B': ['C'], 'C': ['A', 'D'], 'D': ['A']}
if __name__ == '__main__':
    graph = get_graph()
    print(graph.items)
    print(is_tree(graph))
    print(graph.convert_to_undirected())
    print(get_leafs(graph))
    print('has root')
    has_root_result = has_root(graph.items)
    print(has_root_result)
