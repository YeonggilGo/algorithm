# O(n^2)

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

a = [3,2,1,4]
bubble_sort(a)
print(a)
