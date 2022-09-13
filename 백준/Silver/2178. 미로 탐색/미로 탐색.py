# BOJ_2178 미로 탐색 문제풀이
# 2022-09-13
def bfs(s):
    global visited
    global cnt
    global start
    visited.append(s)
    start = 0
    while True:
        end = len(visited)
        cnt += 1
        for k in range(start, end):
            for i, j in d:
                if visited[k][0] + i == N - 1 and visited[k][1] + j == M - 1:
                    return cnt + 1

                if 0 <= visited[k][0] + i < N and 0 <= visited[k][1] + j < M:
                    if board[visited[k][0] + i][visited[k][1] + j] == 1:
                        visited.append([visited[k][0] + i, visited[k][1] + j])
                        board[visited[k][0] + i][visited[k][1] + j] = 2
        start = end


N, M = map(int, input().split())

board = [[] for _ in range(N)]
visited = []
start = 0
cnt = 0

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for n in range(N):
    miro = input()
    for i in miro:
        board[n].append(int(i))
print(bfs([0, 0]))