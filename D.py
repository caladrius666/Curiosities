n, m = [int(x) for x in input().split()]

V = [[]*n for i in range(n)]

for i in range(m):
    a, b = [int(x) for x in input().split()]
    V[a].append(b)
    V[b].append(a)

Color = [0] * n
IsBipartite = True

def DFS(start, IsBipartite):
    for u in V[start]:
        if Color[u] == 0:
            Color[u] = 3 - Color[start]
            DFS(u, IsBipartite)
        if Color[u] == Color[start]:
            IsBipartite = False
            print('NO')
            exit()

for i in range(n):
    if Color[i] == 0:
        Color[i] = 1
        DFS(i, IsBipartite)

for i in range(len(Color)):
    if Color[i] == 1:
        print(i, end=' ')
