import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

# 알고리즘
# 1. 각각 왼쪽과 오른쪽부터 값을 비교하는 i,j를 정의[hint : Quick 정렬 코드참고]
# 2. i,j 가 점점 좁혀오면서 두값의 합을 비교
# [-8,-7,-6,-5,0,1,2,3,4,5,6,7,8]

minv=1e9
left=0
right=N-1
while left<right:
    sum=arr[left]+arr[right]
    if abs(sum)<abs(minv): #최소값 갱신
        minv=sum
    
    #음수 , 0가 가깝게 하려면 left증가
    if sum<0:
        left+=1
    else:
        right-=1 #양수

print(minv)
