# TC - O(V*V) SC - O(V)
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def primMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])
    
    def minKey(self, weight, visited):
        minn = float('inf')

        for i in range(self.V):
            if weight[i] < minn and visited[i] == 0:
                minn = weight[i]
                min_index = i
        return min_index
    
    def Prim(self, src):
        weight = [float('inf')] * self.V
        visited = [0]*self.V
        parent = [None]*self.V

        weight[src] = 0
        parent[src] = -1
        for i in range(self.V):
            u = self.minKey(weight, visited)

            visited[u] = 1

            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == 0 and weight[v] > self.graph[u][v]:
                    weight[v] = self.graph[u][v]
                    parent[v] = u

        self.primMST(parent)

# Driver's code
if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    g.Prim(0)