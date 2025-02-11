from collections import defaultdict, deque
n = 3
l = [[1,3],[2,3]]
# l = [[1,2],[2,3],[3,1]]

indeg = defaultdict(int)
graph = defaultdict(list)

for a,b in l:
    graph[a].append(b)
    indeg[b] += 1

q = deque()

for i in range(1,n+1):
    if indeg[i] == 0:
        q.append(i)

ans= 0
pattern = []

while q:
    ans += 1

    for _ in range(len(q)):
        el = q.popleft()
        n-=1
        pattern.append(el)
        for nei in graph[el]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
if n==0:
    print(ans)
    print(pattern)
else:
    print('Loop is there')