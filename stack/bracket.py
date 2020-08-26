for tc in range(1, 11):
    N = int(input())
    brackets = input()
    stack = []
    ans = 1
    bracket_dict = {']': '[', '}': '{', '>': '<', ')': '('}
    for bracket in brackets:
        if bracket in bracket_dict.values():
            stack.append(bracket)
        else:
            if not stack or stack[-1] != bracket_dict[bracket]:
                ans = 0
                break
            else:
                stack.pop()
    print(f'#{tc} {ans}')
