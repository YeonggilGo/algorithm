import random


def dfs(cnt, min_order, sum, stack):
    global minValue
    if cnt == N:
        minValue = min(sum, minValue)
        return

    if min_order in visited[cnt]:
        print(visited,min_order,cnt)
        return
    visited[cnt].append(min_order)

    order = [cards[cnt].index(sorted(cards[cnt])[i]) for i in range(4)]
    for i in range(4):
        for j in range(i + 1, 4):
            if order[j] == order[i]:
                order[j] += 1

    print(cnt, sum, min_order, cards[cnt], order, stack)
    if not stack or stack[-1] != order[min_order]:
        stack.append(order[min_order])
        dfs(cnt + 1, 0, sum + cards[cnt][order[min_order]], stack)
        visited[cnt].pop(0)
    elif stack[-1] == order[min_order]:

        # 이번 학생의 카드를 다음 작은걸로 바꿔서 재귀
        if min_order < 3:
            dfs(cnt, min_order + 1, sum, stack)
            while len(stack) >= cnt + 1:
                stack.pop()

        # # 전 학생의 카드를 다음 작은 걸로 바꿔서 재귀
        if stack[-1] < 3:  # 이미 가장 클경우는 패스
            if cnt > 1:
                tmp = stack.pop()
                dfs(cnt - 1, order.index(tmp) + 1, sum - cards[cnt - 1][tmp], stack)


N = 10
cards = []
for _ in range(4):
    card = list(range(1, N + 1))
    random.shuffle(card)
    cards.append(card)
cards = list(map(list, zip(cards[0], cards[1], cards[2], cards[3])))
visited = [[] for _ in range(N)]
minValue = N * N + 1
dfs(0, 0, 0, [])
for i in range(N):
    print(cards[i])

print(minValue)
