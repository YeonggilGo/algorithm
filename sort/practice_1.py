data = [7,4,2,0,0,6,0,7,0]
box = []
top = max(data)
for i in range(len(data)):
    box.append([1]*data[i] + [0]*(top-data[i]))

new_box = []
for i in range(top):
    tmp = 0
    for j in range(len(data)):
        if box[j][i]:
            tmp += 1
    new_box.append(tmp)

print(new_box)
print(1+1)