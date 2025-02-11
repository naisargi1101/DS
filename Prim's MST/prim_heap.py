# TC: O(E*log(E)) SC: O(V*V)
from heapq import heappush, heappop
from collections import defaultdict

def Prim(V, edges):
    adj = defaultdict(list)
    
    for u, v, w in edges:
        adj[u].append((v,w))
        adj[v].append((u,w))
    
    pq = [(0,0)]
    visited = [0]*V
    res = 0

    while pq:
        wt, node = heappop(pq)
        if visited[node]:
            continue
        res += wt
        visited[node] = 1
        for neigh, w in adj[node]:
            if not visited[neigh]:
                heappush(pq, (w,neigh))
    return res

if __name__ == "__main__":
    graph = [[0, 1, 5],
             [1, 2, 3],
             [0, 2, 1]]
    # Function call
    print(Prim(3, graph))