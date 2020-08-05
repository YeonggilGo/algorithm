# Search



|  알고리즘  | 평균 시간 | 최악 시간 | 기법 |            비고            |
| :--------: | :-------: | :-------: | :--: | :------------------------: |
| Sequential |   O(n)    |   O(n)    |      | 쉽지만 n이 커지면 비효율적 |
|   Binary   |  O(logn)  |  O(logn)  |      |                            |
|            |           |           |      |                            |



### Sequential Search

> 순회하며 키 값이 있는지 탐색
>
> 평균 비교회수 = (1/n)*(1+2+3+...+n) = (n+1)/2
>
> O(n)

```python
def sequential_search(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n:
        return i
    else:
        return -1

# 정렬이 되어있다면

def sequential_search2(a, n, key):
    i = 1
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key:
        return i
    else:
        return -1
```



### Binary Search

> 자료의 가운데에 있는 항목과 키값을 비교하여 검색 위치를 결정. 정렬이 필요
>
> 

```python
def binary_search(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == key:
            return True
        elif a[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return False


def binary_search2(a, low, high, key):
    if low > high:
        return False
    else:
        mid = (high + low) // 2
        if key == a[mid]:
            return True
        elif key < a[mid]:
            return binary_search2(a, low, mid - 1, key)
        elif a[mid] < key:
            return binary_search2(a, mid + 1, high, key)

```

