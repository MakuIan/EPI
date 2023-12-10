'''
EPR 6 - Exercise 2
'''
__author__ = '8175858, Braun'
import ue06_functions as f


# {0: [1, 2], 1: [], 2: []}
# {0:[1,2],1:[],2:[],3:[2]}
# {'A': ['B'], 'B': ['C'], 'C': ['A', 'D'], 'D': ['A']}
if __name__ == '__main__':
    graph = f.get_graph()
    print('your graph:', graph.items)
    print('graph is tree:', f.is_tree(graph))
    print('leafs:', f.get_leafs(graph))
    root = f.has_root(graph.items)
    print('has root:', root[0])
    if root[0]:
        print(f'Node {root[1]} is root.')
    else:
        print('No root found.')
