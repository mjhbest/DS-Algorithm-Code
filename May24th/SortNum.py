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
            # 왼쪽 리스트가 비어있다면 그대로 오른쪽 리스트를 붙이기
            mergedList += right

        elif len(right) == 0:
            # 오른쪽 리스트가 비어있다면 그대로 왼쪽 리스트를 붙이기
            mergedList += left

    return mergedList

def sort(number):
    num_list = [int(c) for c in str(number)]
    num_list = merge_sort(num_list)
    num_list = [num_list[i] for i in range(len(num_list)-1,-1,-1)]
    num_list = [str(n) for n in num_list]
    return "".join(num_list)

number = int(input())
print(sort(number))
