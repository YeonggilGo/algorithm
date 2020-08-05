def select(list, k):
    for i in range(k):
        mid_idx = i
        for j in range(i + 1, len(list)):
            if list[mid_idx] > list[j]:
                mid_idx = j
        list[i], list[mid_idx] = list[mid_idx], list[i]
    return list[k - 1]
