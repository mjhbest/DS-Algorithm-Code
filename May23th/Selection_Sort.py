def selection_sort(a):
    ## [실습] ##
    for i in range(0, len(a)):
        ## [실습] ##
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                ## [실습] ##
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]


a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]

print('정렬 전:\t', end='')
print(a)

selection_sort(a)

print('정렬 후:\t', end='')
print(a)
