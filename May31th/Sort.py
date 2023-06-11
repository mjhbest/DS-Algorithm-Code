import sys
# input() 과 sys.stdin.readline() 을 활용해봅시다.

# Hint :
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

# Sort()
num.sort()

for i in num:
    print(i)
