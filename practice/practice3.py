inp = '''9 20 2 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14
'''
board = []
for i in range(5):
    board.append(list(map(int, inp.split('\n')[i].split())))

snail = [[0 for i in range(7)] for j in range(7)]
for i in range(5):
    for j in range(5):
        snail[j + 1][i + 1] = board[j][i]

order = []
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
pos = [1, 1]
num = []
dir = 0
for i in range(25):
    order.append(pos)
    num.append(snail[pos[0]][pos[1]])
    while True:
        ny = pos[0] + dy[dir]
        nx = pos[1] + dx[dir]
        if snail[ny][nx] == 0 or snail[ny][nx] in num:
            dir = (dir + 1) % 4
            if i == 24:
                break
        else:
            pos = [ny, nx]
            break
num.sort()
for i in range(len(order)):
    snail[order[i][0]][order[i][1]] = num[i]

for j in range(5):
    for i in range(5):
        print(snail[j + 1][i + 1], end = ' ')
    print()
