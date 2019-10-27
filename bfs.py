def bfs(G, x, y, visited, m, n):
    queue = [(x, y)]
    ans = []
    while queue:
        i, j = queue.pop()
        if (0 <= i < m) and (0 <= j < n) and (not visited[i][j]) and G[i][j] == 1:
            queue.insert(0, (i + 0, j - 1)) # left
            queue.insert(0, (i + 0, j + 1)) # right
            queue.insert(0, (i - 1, j + 0)) # top
            queue.insert(0, (i + 1, j + 0)) # bottom
            ans.append((i, j))
            visited[i][j] = True
    return ans

    
if __name__ == '__main__':
    graph = [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0]
    ]
    
    m = len(graph)
    n = len(graph[0])
    visited = [[False for j in range(n)] for i in range(m)]
    res = bfs(graph, 0, 4, visited, m, n)
    print(res)

