# TC - O(V*V) SC - O(N)

from collections import deque
class Graph:
    adj = []

    def __init__(self, v, e):
        self.v = v
        self.e = e
        Graph.adj = [[0] * v for i in range(v)]
    
    def addEdge(self, start, e):
        Graph.adj[start][e] = 1
        Graph.adj[e][start] = 1
    
    def BFS(self, start):
        q = deque([start])
        visited = [0]*self.v
        visited[start] = 1
        
        while q:
            node = q.popleft()
            print(node)
            for i in range(self.v):
                if Graph.adj[node][i] == 1 and visited[i] == 0:
                    q.append(i)
                    visited[i] = 1
            

# Driver code
v, e = 5, 4
 
# Create the graph
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(1, 3)
 
# Perform BFS
G.BFS(0)