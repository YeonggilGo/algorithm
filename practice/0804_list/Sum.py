import sys

sys.stdin = open('Sum.txt', 'r')
for _ in range(10):
    tc = int(input())
    numbers = []
    for i in range(100):
        numbers.append(list(map(int, input().split())))

    ans = 0

    # 가로
    for j in range(100):
        sum_ = sum(numbers[j])
        ans = sum_ if sum_ > ans else ans

    # 세로
    for i in range(100):
        sum_ = 0
        for j in range(100):
            sum_ += numbers[j][i]
        ans = sum_ if sum_ > ans else ans

    # 대각선
    sum1 = 0
    sum2 = 0
    for i in range(100):
        sum1 += numbers[i][i]
        sum2 += numbers[i][99-i]
    ans = max(sum1,sum2,ans)

    print('#{} {}'.format(tc, ans))
