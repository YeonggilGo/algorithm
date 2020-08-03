# 6장의 카드가 연속적인 카드 세장과 같은 카드 세장으로 이루어지면
# Baby-gin 이라고 부른다.

def is_baby_gin(numbers):
    numbers = sorted(list(map(int,numbers)))


    front = numbers[:3]
    end = numbers[3:]
    if front[0] == front[1] == front[2]:
        pass
    elif front[1] == front[0] + 1 and front[2] == front[1] + 1:
        pass
    else:
        return False

    if end[0] == end[1] == end[2]:
        pass
    elif end[1] == end[0] + 1 and end[2] == end[1] + 1:
        pass
    else:
        return False

    return True
print(is_baby_gin((input())))