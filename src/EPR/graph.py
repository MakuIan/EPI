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
