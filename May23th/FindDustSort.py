dust_data = []
for i in range(5):
    dust_data.append(int(input()))

# 선택 정렬


def selection_sort(a):
    for i in range(0, len(a)):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]
    return a

# 삽입 정렬


def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
    return a


# 오름차순 정렬하세요.
sort_data = dust_data
print(insertion_sort(sort_data))
