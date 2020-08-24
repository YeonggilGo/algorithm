#4864

def find_largest_index(str, latter):
    for i in range(len(str)-2,-1,-1):
        if str[i] == latter:
            return i

T = int(input())


for tc in range(1, T + 1):
    tar = input()
    given = input()
    res = 0
    pos = len(tar) - 1

    while pos <= len(given) - 1:
        find = True

        if tar[-1] == given[pos]:
            for i in range(1, len(tar)):
                if tar[len(tar) - i - 1] != given[pos - i]:
                    find = False
                    break
        else:
            find = False
            
        if find:
            res = 1
            break
        else:
            if given[pos] == tar[-1]:
                if given[pos] in tar[:-1]:
                    pos += len(tar) - find_largest_index(tar, given[pos]) - 1
                else:
                    pos += len(tar)
            elif given[pos] in tar:
                pos += len(tar) - find_largest_index(tar, given[pos]) - 1
                find = False
            else:
                pos += len(tar)
                find = False

    print(f'#{tc} {res}')