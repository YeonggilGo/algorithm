N = 5
board = [[1 if j == 0 or j == 4 or i == 0 or i == 4 else 0 for i in range(5)] for j in range(5)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(4):
            ny = j + dy[k]
            nx = i + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                ans += board[ny][nx] - board[j][i] if board[ny][nx] >= board[j][i] else board[j][i] - board[ny][nx]

print(ans)
