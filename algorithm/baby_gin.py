# 6장의 카드가 연속적인 카드 세장과 같은 카드 세장으로 이루어지면
# Baby-gin 이라고 부른다.

def is_baby_gin(numbers):
    c = [0] * 10
    for number in numbers:
        c[int(number)] += 1

    run, tri = 0, 0
    i = 0
    while i < 10:
        if c[i] >= 3:
            tri += 1
            c[i] -= 3
            continue

        if i<8:
            if all([c[i], c[i + 1], c[i + 2]]):
                run += 1
                for j in range(3):
                    c[i+j] -= 1
                continue
        i += 1
    if run + tri == 2:
        return True
    else:
        return False


print(is_baby_gin((input())))
