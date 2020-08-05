# 10개의 정수중 부분집합의 합이 0이 되는 것이 존재하는지 계산하라
arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]

n = len(arr)

cnt = 0

for i in range(1 << n):
    if sum([arr[j] for j in range(n + 1) if i & (1 << j)]) == 0:
        cnt += 1

cnt -= 1  # 공집합
print('cnt : {}'.format(cnt))
