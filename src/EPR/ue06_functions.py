'''
EPR 06 - Aufgabe 2
'''
__author__ = '8175858, Braun'
import ast
from graph import Graph


def get_graph():
    '''
    Takes in a graph in form of an adjacency list and returns it.
    Uses ast.literal_eval to convert the input string to a dictionary instead of just eval,
    because eval only works with numbers
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
    edges = sum(len(edges) for edges in ugraph.values()) // 2
    if edges != vertices - 1:
        return False
    return graph.is_cyclic()


def get_leafs(graph):
    '''
    Takes in a graph and returns a set of leafs as a set
    '''
    leafs = set()
    for vertex, edges in graph.items.items():
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
    print('your graph:', graph.items)
    print('graph is tree:', is_tree(graph))
    print('leafs:', get_leafs(graph))
    root = has_root(graph.items)
    print('has root:', root[0])
    if root[0]:
        print(f'Node {root[1]} is root.')
    else:
        print('No root found.')
