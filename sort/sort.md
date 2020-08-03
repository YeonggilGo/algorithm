# Sort



### Bubble Sort

> 배열을 2중 순회하며 크기 비교를 통해 정렬
>
> O(n^2)

```python
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
```

