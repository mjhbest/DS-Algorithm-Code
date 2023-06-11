graph = [
    [], #0
    [2, 3, 8], #1
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
    visited[v] = True
    #2. v가 더 깊게 들어갈 수 있는 후보 경로 추적
    for w in graph[v]:
    #3. 해당 노드가 이미 방문한적 있는지 확인
        if not visited[w]:
    #4. 없다면 해당 노드아래로 dfs진행
            dfs(graph,w)

# 0번 노드가 없으니 1번 노드부터 탐색
for i in range(9):
    dfs(graph, i)

for i in range(9):
    if visited[i]:
        print(i)
