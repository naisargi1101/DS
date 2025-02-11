# TC - O(V + E) SC - O(V)

from collections import deque
def bfs(adj, src, V):
    q = deque([src])
    visited = [0]*V
    visited[src] = 1
    while q:
        node = q.popleft()
        print(node)
        for neigh in adj[node]:
            if visited[neigh] == 0:
                visited[neigh] = 1
                q.append(neigh)
    
# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# Example usage
if __name__ == "__main__":
  
    # Number of vertices in the graph
    V = 5

    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # Add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    # Perform BFS traversal starting from vertex 0
    print("BFS starting from 0: ")
    bfs(adj, 0, V)