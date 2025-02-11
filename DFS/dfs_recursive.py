# TC - O(V+E) SC - O(V+E)
def dfsUtil(adj, src, visited):
    visited[src] = 1
    print(src)
    for neigh in adj[src]:
        if visited[neigh] == 0:
            dfsUtil(adj, neigh, visited)

def dfs(adj, src):
    visited = [0]*len(adj)
    dfsUtil(adj, src, visited)

def add_edge(adj, s, d):
    adj[s].append(d)
    adj[d].append(s)

if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 1
    print("DFS from source:", source)
    dfs(adj, source)