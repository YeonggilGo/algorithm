#4865

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    str1 = list(set(list(str1)))

    res = dict()

    for i in range(len(str1)):
        if str1[i] in str2:
            res[str1[i]] = str2.count(str1[i])

    print(f'#{tc} {max(res.values())}')