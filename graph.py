from collections import deque    # 'deque' class from 'collections' module can be used to implement a queue. 

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(1, num_vertices+1)}
        self.Visited_DFS = [False] * (num_vertices + 1)
        self.Visited_BFS = [False] * (num_vertices + 1)
        self.component = [0] * (num_vertices + 1)       # An array that holds an INT value which indicates the component a node belongs to
        self.parent = [-1] * (num_vertices + 1)       # An array that holds the parent of each node in a graph.
        # The parent array will help us to track the shortes path between start node(s) and end node(e)
        self.count = 0


    def add_edge(self, u, v, weight = 0):               # 0 is the default value of weighted edge if it is not passed
        if u == v:                                      # cyclic node  
            self.adj_list[u].append((v, weight))
        else:
            self.adj_list[u].append((v, weight))    
            self.adj_list[v].append((u, weight))            # comment this line if it is a directed graph

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, end="")
            for neighbor in self.adj_list[vertex]:      # loop iterates over the values in the list of each key.
                print(" -> ({}, {})".format(neighbor[0], neighbor[1]), end="")
            print()
    
    def DFS(self, index):
        if self.Visited_DFS[index]:
            return
        self.Visited_DFS[index] = True
        self.component[index] = self.count
        # print(index, " --> ", end=' ')
        for next in self.adj_list[index]:               # loop iterates over the values in the list of each key.
            self.DFS(next[0])                           # next[0]: The next value to apply dfs at, next[1]: The weight of the associated edge


    def find_strong_components(self):
        for index in range(1, self.num_vertices+1):
            if not self.Visited_DFS[index]:
                self.count += 1
                self.DFS(index)
        return self.count
    
    def BFS(self, start):
        q = deque()
        q.append(start)
        self.Visited_BFS[start] = True
        while len(q) != 0:
            parent = q.popleft()
            # print(parent, " --> ", end = '')
            for next in self.adj_list[parent]:
                if not self.Visited_BFS[next[0]]:
                    self.Visited_BFS[next[0]] = True
                    q.append(next[0])
                    self.parent[next[0]] = parent
        return

    def find_shortes_path (self, s, e):
        self.BFS(s)
        path = ""
        at = e
        while at != -1:
            if at == s: 
                path += str(at)
                break
            path += str(at)
            at = self.parent[at]
        # print(path)
        path = ''.join(reversed(path))
        if path[0] == str(s):
            return path
        return 


g = Graph(7)
g.add_edge(1, 7)
g.adj_list[1].insert(0, ())
g.add_edge(2, 7)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(3, 6)
g.add_edge(4, 5)
print(g.adj_list)
# print(g.find_strong_components())
# print(g.component[7])
print()
for index in g.find_shortes_path(2, 5):
    print(index, " --> ", end = '')
# g.print_graph()
# print(g.Visited[4])

"""

from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)  # or do any other processing with the node
            
            # Add all the unvisited neighbors of the current node to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# The complete graph represented as an adjacency list
graph = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['A', 'B', 'C', 'D']
}

start_node = 'A'  # Choose the starting node

bfs(graph, start_node)
"""