class UnionByRank:
    def __init__(self, v):
        self.rank = [0]*v
        self.parent = [i for i in range(v)]
    
    # TC - O(lov V)
    def findParent(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]
    
    #TC - O(1)
    # u and v are parents of itself
    def union(self, u, v):
        if self.rank[v] > self.rank[u]:
            u, v = v, u
        
        self.parent[v] = u

        if self.rank[u] == self.rank[v]:
            self.rank[u] += 1


    
