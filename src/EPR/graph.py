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

    def is_cyclic_util(self, visited: dict, current) -> bool:
        if visited[current] is True:
            return True
        visited[current] = True
        flag = False
        for i in self.items[current]:
            flag = self.is_cyclic_util(visited, self.items[current][i])
            if flag is True:
                return True
        return False

    def is_cyclic(self) -> bool:
        visited = {node: False for node in self.items}
        flag = False  # keep track of wheter a cycle exists
        for node, edges in self.items.items():
            visited[node] = True
            for e in edges:
                flag = self.is_cyclic_util(visited, self.items[node][e])
                if flag is True:
                    return True
            visited[node] = False
        return False
