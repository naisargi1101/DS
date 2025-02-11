from heapq import heappop, heappush

# TC: O(E*logV)  SC: O(V*V)
class Graph:
    def __init__(self, V):
        self.V = V  # No. of vertices
        self.adj = [[] for _ in range(V)]  # In a weighted graph, store vertex and weight pair for every edge
    
    
    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def shortest_path(self, src):
        visited = [0]* self.V
        dist = [float('inf')]*self.V

        pq = [(0,src)]       
        dist[0] = 0

        while pq:
            d, node = heappop(pq)
            visited[node] = 1
            
            for v, w in self.adj[node]:
                if visited[v] == 0 and dist[v] > w + d:
                    dist[v] = w + d
                    heappush(pq, (w+d, v))
            
        # Print shortest distances
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

# Driver program to test methods of the graph class
if __name__ == "__main__":
    # Create the graph given in the above figure
    V = 9
    g = Graph(V)

    # Making the above-shown graph
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    g.shortest_path(0)