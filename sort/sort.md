# Sort

### Bubble Sort

> 배열을 2중 순회하며 크기 비교를 통해 정렬
>
> 코딩이 가장 손쉽다.
>
> O(n^2)

```python
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
```



### Counting Sort

> 각 항목이 몇 개씩 있는지 세어 선형시간에 정렬. 정수만 가능. max : k값을 알아야함
>
> n이 비교적 작을 때만 가능하다.
>
> O(n+k)

```python
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
```

> 

```python
def my_counting_sort(A, k):
    # A : 입력 배열
    # C : 카운트 배열
    C = [0] * (k + 1)

    for i in range(len(A)):
        C[A[i]] += 1

    res = []
    for i in range(len(C)):
        if C[i]:
            res.extend(([i]*C[i]))
    return res
```



