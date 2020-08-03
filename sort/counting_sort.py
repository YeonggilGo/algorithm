# O(n + k)

def counting_sort(A, k):
    # A : 입력 배열
    # C : 카운트 배열
    C = [0] * (k+1)

    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    res = [0] * len(A)
    for i in range(len(res) - 1, -1, -1):
        res[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return res


def my_counting_sort(A, k):
    # A : 입력 배열
    # C : 카운트 배열
    C = [0] * (k + 1)

    for i in range(len(A)):
        C[A[i]] += 1

    res = []
    for i in range(len(C)):
        if C[i]:
            res.extend(([i] * C[i]))
    return res


a = counting_sort([0,4,1,3,1,2,4,1], 4)
print(a)
