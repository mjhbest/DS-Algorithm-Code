from random import *
from copy import copy
import time

def merge_sort(arr):
    """
    arr : 정렬 할 배열 
    ---
    return :  정렬 된 배열
    """
    if len(arr) <= 1: # 종료조건
        return arr 
    mid = len(arr) // 2
    
    leftList = arr[:mid]
    rightList = arr[mid:]

    leftList = merge_sort(leftList) # sort
    rightList = merge_sort(rightList) # sort
    
    mergedList = merge(leftList,rightList)
    return mergedList

def merge(left, right):
    # leftList, rightList는 이미 정렬이 되어있다.
    mergedList = []
    total_len = len(left) + len(right)

    while len(mergedList) < total_len:
        if len(left) > 0 and len(right) > 0 : 
            # left & right 모두 하나 이상의 값이 남아있을때는 비교
            if left[0] <= right[0]:
                mergedList.append(left.pop(0))
            else:
                mergedList.append(right.pop(0))

        elif len(left) == 0:
            # 왼쪽 리스트가 비어있다면 그래도 오른쪽 리스트를 붙이기
            mergedList += right

        elif len(right) == 0:
            # 오른쪽 리스트가 비어있다면 그래도 왼쪽 리스트를 붙이기
            mergedList += left
    return mergedList



def quick_sort(a, low, high):
    """
    a : array [List]
    low : 정렬 할 가장 왼쪽값의 index [INT]
    hight : 정렬 할 가장 오른값의 index [INT]
    """
    if low < high:
        pivot = partition(a, low, high)
        quick_sort(a, low, pivot-1)
        quick_sort(a, pivot+1, high)
    return a


def partition(a, pivot, high):
    """
    a : array [List]
    pivot : pivot값의 index [INT]
    hight : 정렬 할 가장 오른값의 index [INT]
    """
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j


def bubble_sort(unsorted, N):
    for i in range(N-1, 0, -1):  # i : 어디까지 검사하는가?
        for j in range(i):  # j : 버블의 위치
            if unsorted[j] > unsorted[j+1]:  # 버블 왼쪽값 > 버블 오른쪽 => 역전상태!
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]


arr = [3, 6, 1, 2, 3, 34, 68, 3, 44, 23, 12, 4, 466]

arr = quick_sort(arr, 0, len(arr)-1)
print(arr)


# Test
num_samples = 1000
samples = []
for i in range(num_samples):
    samples.append(randint(1, 10000))
samples_test1 = copy(samples)
samples_test2 = copy(samples)
samples_test3 = copy(samples)
samples_test4 = copy(samples)
print("Sample 생성 완료")

# bubble
start_time1 = time.time()
bubble_sort(samples_test1, len(samples_test1))
end_time1 = time.time()
print("bubble   :   ",  end_time1 - start_time1)

# quick
start_time2 = time.time()
quick_sort(samples_test2, 0, len(samples_test2)-1)
end_time2 = time.time()
print("quick    :   ", end_time2 - start_time2)

# list.sort()
start_time3 = time.time()
samples_test3.sort()
end_time3 = time.time()
print("builtin  :   ", end_time3 - start_time3)

# list.sort()
start_time4 = time.time()
merge_sort(samples_test4)
end_time4 = time.time()
print("merge  :   ", end_time4 - start_time4)

# samples.sort()
# samples_test = quick_sort(samples_test,0,len(samples_test)-1)
# for i in range(len(samples)):
#     if samples[i] != samples_test[i]:
#         print("Fail")
#         exit(-1)

# print("Pass")
