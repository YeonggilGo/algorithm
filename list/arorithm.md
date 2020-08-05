# List

### Bit operation

- `&` : and , `|` : or ,  `<<` : bit를 왼쪽으로 , `>>` : bit를 오른쪽으로
- `1 << n ` : 2^n, 원소가 n개일 경우 모든 부분집합의 수를 의미한다.
  - ` i & (1 << j ) `: i의 j번째 비트가 1인지 아닌지를 return 한다.



### Subset

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)  # n : 원소의 개수

for i in range(1 << n):  # 1<<n : 부분집합의 개수
    for j in range(n + 1):  # 원소의 수만큼 비트를 비교함
        if i & (i << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end = ', ')
    print()
print()
```

