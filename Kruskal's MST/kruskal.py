# TC - O(E * logE + E * logV) SC - O(V+E)
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parent = [i for i in range(self.V)]
        self.rank = [0]*self.V

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def findParent(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        if self.rank[v] > self.rank[u]:
            u,v = v, u
        
        self.parent[v] = u

        if self.rank[u] == self.rank[v]:
            self.rank[u] += 1
    
    def KruskalMST(self):
        # O(E * logE)
        self.graph.sort(key = lambda item:item[2])
        mstWeight = 0
        edges = []

        # union find for all edges TC - O(E*logV)
        for u,v,w in self.graph:
            pu = self.findParent(u)
            pv = self.findParent(v)

            if pu!=pv:
                self.union(pu,pv)
                edges.append((u,v))
                mstWeight += w
                if len(edges) == self.V - 1:
                    break
        print(mstWeight)
        print(edges)


# Driver code
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call
    g.KruskalMST()