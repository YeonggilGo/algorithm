# Sort



| 알고리즘  | 평균 시간 | 최악 시간 |    기법     |              비고              |
| :-------: | :-------: | :-------: | :---------: | :----------------------------: |
|  Bubble   |  O(n^2)   |  O(n^2)   | 비교와 교환 |          코딩이 쉽다.          |
| Counting  |  O(n+k)   |  O(n+k)   |   비교환    |        n이 작아야 가능         |
| Selection |  O(n^2)   |  O(n^2)   | 비교와 교환 |    회수가 위 두개보다 적음     |
|   Quick   | O(nlogn)  |  O(n^2)   |  분할 정복  |      평균적으로 가장 빠름      |
| Insertion |  O(n^2)   |  O(n^2)   | 비교와 교환 |       n이 작으면 효율적        |
|   Merge   | O(nlogn)  | O(nlogn)  |  분할 정복  | 연결 리스트의 경우 가장 효율적 |



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



### Selection Sort

> 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
>
> selection algorithm을 전체 자료에 적용
>
> O(n^2)

```python
def selection_sort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
```

