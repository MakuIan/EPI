# def isCylclic_util(adj:list, visited:list, curr:int) -> bool :
#     if visited[curr] == True:
#         return True

#     visited[curr] = True
#     flag = False
#     for

class Graph:
    def __init__(self):
        self.items = {}

    def init_keys(self, key):
        self.items[key] = []

    def add(self, vertex, edges):
        if vertex in self.items:
            self.items[vertex].append(edges)

    def get_num_edges(self):
        return sum(len(edges) for edges in self.items.values())

    def get_num_vertices(self):
        return len(list(self.items.keys()))

    def convert_to_undirected(self):
        undirected_graph = {v: e for v, e in self.items.items()}
        for vertice, edges in self.items.items():
            for edge in edges:
                if vertice not in undirected_graph[edge]:
                    undirected_graph[edge].append(vertice)
        return undirected_graph

    def isCyclic_util(self, v, visited, parent, ugraph):
        visited[v] = True
        for edges in ugraph[v]:
            if visited[edges] is False:
                if self.isCyclic_util(edges, visited, v, ugraph) is True:
                    return True
            elif parent != edges:
                return True
        return False

    def isCyclic(self):
        visited = {vertice: False for vertice in self.items}
        ugraph = self.convert_to_undirected()
        for vertex, edges in ugraph.items():
            if visited[vertex] is False:
                if self.isCyclic_util(vertex, visited, -1, ugraph) is True:
                    return True
        return False
