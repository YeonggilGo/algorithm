# 선택의 경우에 최적해를 찾아가는 알고리즘
# 예시 : 거스름돈 줄이기

money = int(input())
change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
ans = [0] * len(change)
for i in range(len(change)):
    if money // change[i] >= 1:
        ans[i] += money//change[i]
        money %= change[i]

ans = ' '.join(list(map(str, ans)))
print(ans)
