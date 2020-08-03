# Algorithm

### Exaustive Search

> 생각할 수 있는 모든 경우의 수를 나열해보고 확인. Brute force라고도 부름.
>
> 경우의 수가 작을 때 유리. 시험 등에서 우선 BF로 접근하여 답을 확인후 다른 알고리즘을 사용하자



### Greedy Algorithm

> 여러 경우 중 하나를 결정 할 때마다 순간에 최적해를 선택한다.
>
> 최종적인 해답이 최적이라는 보장은 없다.

```python
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
```

