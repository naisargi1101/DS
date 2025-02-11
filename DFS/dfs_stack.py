# TC - O(V + E) SC - O(V)
def dfs(adj, src):
    visited = [0]*len(adj)

    st = [src]
    while st:
        node = st.pop()
        
        if not visited[node]:
            print(node)
            visited[node] = 1

        for neigh in adj[node]:
            if visited[neigh] == 0:
                st.append(neigh)


def add_edge(adj, s, d):
    adj[s].append(d)
    adj[d].append(s)

if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 0], [0, 2], [2, 1], [1, 4], [0, 3]]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 0
    print("DFS from source:", source)
    dfs(adj, source)