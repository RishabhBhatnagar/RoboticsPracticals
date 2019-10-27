def dfs(G, i, j, visited, m, n):
    ans = []
    if (0 <= i < m) and (0 <= j < n)and (not visited[i][j]) and G[i][j] == 1:
        visited[i][j] = True
        ans.append((i, j))
        ans.extend(dfs(G, i + 0, j - 1, visited, m, n))  # left
        ans.extend(dfs(G, i + 0, j + 1, visited, m, n))  # right
        ans.extend(dfs(G, i - 1, j + 0, visited, m, n))  # top
        ans.extend(dfs(G, i + 1, j + 0, visited, m, n))  # bottom
    return ans



# alternative implementation


def dfs(G, i, j, visited, m, n):
    if (0 <= i < m) and (0 <= j < n)and (not visited[i][j]) and G[i][j] == 1:
        visited[i][j] = True
        return [
            (i, j),
            *dfs(G, i + 0, j - 1, visited, m, n),  # left
            *dfs(G, i + 0, j + 1, visited, m, n),  # right
            *dfs(G, i - 1, j + 0, visited, m, n),  # top
            *dfs(G, i + 1, j + 0, visited, m, n)   # bottom
        ]
    return []


# another alternative implementation algorithm

def dfs(G, x, y, visited, m, n):
    # iterative version:
    stack = [(x, y)]
    ans = []
    while stack:
        i, j = stack.pop()
        if (0 <= i < m) and (0 <= j < n)and (not visited[i][j]) and G[i][j] == 1:
            stack.append((i + 0, j - 1))  # left
            stack.append((i + 0, j + 1))  # right
            stack.append((i - 1, j + 0))  # top
            stack.append((i + 1, j + 0))  # bottom
            visited[i][j] = True
            ans.append((i, j))
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
    res = dfs(graph, 0, 4, visited, m, n)
    print(res)

