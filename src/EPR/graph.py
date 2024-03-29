'''
Graph class for EPR UE06
'''

import copy

__author = '8175858, Braun'


class Graph:
    '''
    A class used to represent a directed graph.
    '''

    def __init__(self):
        self.items = {}

    def init_keys(self, key):
        '''
        initializes a key with an empty list in the graph
        '''
        self.items[key] = []

    def add(self, vertex, edges):
        '''
        adds a vertex and its edges to the graph
        '''
        if vertex in self.items:
            self.items[vertex].append(edges)

    def get_num_edges(self):
        '''
        returns the number of edges in the graph
        '''
        return sum(len(edges) for edges in self.items.values())

    def get_num_vertices(self):
        '''
        returns the number of vertices in the graph
        '''
        return len(list(self.items.keys()))

    def convert_to_undirected(self):
        '''
        converts a directed graph to an undirected graph
        '''
        undirected_graph = copy.deepcopy(self.items)
        for vertice, edges in self.items.items():
            for edge in edges:
                if edge not in undirected_graph:
                    undirected_graph[edge] = []
                if vertice not in undirected_graph[edge]:
                    undirected_graph[edge].append(vertice)
        return undirected_graph

    def dfs(self, vertex, visited):
        '''
        A recursive function that uses visited[] to do DFS
        starting from vertex v.
        '''
        visited[vertex] = True
        for neighbor in self.items[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def is_cyclic_util(self, v, visited, parent, ugraph):
        '''
        A recursive function that uses visited[] and parent to detect
        cycle in subgraph reachable from vertex v. Called by isCyclic().
        Visits every neighbour of a vertex using DFS.
        '''
        visited[v] = True

        for neighbor in ugraph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v, ugraph):
                    return True
            elif parent != neighbor:
                return True
        return False

    def is_cyclic(self):
        '''
        Returns true if the graph contains a cycle, else false.
        Initializes visited[], parent to -1 and calls isCyclicUtil()
        Visits every vertex.
        '''
        ugraph = self.convert_to_undirected()
        for vertex, edges in ugraph.items():
            visited = {vertice: False for vertice in ugraph}
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, None, ugraph):
                    return True
        return False

    def is_vertex_isolated(self, vertex):
        '''
        Returns true if the vertex is isolated meaning if it has no neighbours, else false.
        '''
        ugraph = self.convert_to_undirected()
        for edges in ugraph.values():
            if vertex in edges:
                return False
        return True
