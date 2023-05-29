graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문노드
visited = [False] * len(graph)

def dfs(graph, v):
    #1. v 를 visited에 추가

    #2. v가 더 깊게 들어갈 수 있는 후보 경로 추적

    #3. 해당 노드가 이미 방문한적 있는지 확인

    #4. 없다면 해당 노드아래로 dfs진행

# 0번 노드가 없으니 1번 노드부터 탐색
dfs(graph, 1)
