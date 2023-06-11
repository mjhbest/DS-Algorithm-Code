import sys
sys.setrecursionlimit(10**7)

nA, nB = map(int,sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))


# # 1 Python set()
diff = set(A)-set(B)
print(len(diff))
print(sorted(list(diff)))

# 2 전체 탐색 
result = []
for a in A:
    if a not in B:
        result.append(a)
print(len(result))
print(result)

# 3 이진 탐색
def BS(arr,key,start,end): # return : T/F  key in the "list[start:end]" or not
    if start > end: return False
    mid = (start + end)//2
    if key < arr[mid]:
        return BS(arr,key,start,mid-1)
    elif key > arr[mid]:
        return BS(arr,key,mid+1,end)
    else:
        return True
# A의 각 원소들을 돌면서(1), 각 원소가 B에 있는지 탐색한다(2)
# [[단 탐색의 복잡도를 줄이기 위해, 탐색은 이진탐색을 사용한다]]
B.sort() # B 정렬

start = 0
end = len(B)-1

result = []

for a in A:
    if not BS(B,a,0,len(B)-1):
        result.append(a)
print(len(result))
print(sorted(result))
