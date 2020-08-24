#4861

def is_palindrome(str):
    for i in range(len(str) // 2):
        if str[i] != str[-i - 1]:
            return False
    return True

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    board = []
    for i in range(N):
        board.append(list(input()))

    res = ''

    for i in range(N - M + 1):
        for j in range(N):
            if is_palindrome(board[j][i: i + M]):
                res = board[j][i: i + M]

    if not res:
        board = list(map(list, zip(*board)))
        for i in range(N - M + 1):
            for j in range(N):
                if is_palindrome(board[j][i: i + M]):
                    res = board[j][i: i + M]

    res = ''.join(res)
    print(f'#{tc} {res}')
