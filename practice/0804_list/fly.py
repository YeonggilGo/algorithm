T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly = []
    for _ in range(N):
        fly.append(list(map(int, input().split())))

    max_ = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            tmp = 0
            for a in range(M):
                for b in range(M):
                    tmp += fly[j + a][i + b]
            max_ = max_ if max_ > tmp else tmp

    print('#{} {}'.format(tc, max_))
