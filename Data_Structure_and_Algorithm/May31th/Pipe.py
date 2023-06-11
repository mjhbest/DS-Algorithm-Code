# Stack 데이터 구조 : List append, pop을 사용해서 stack 모방

a = list(input())
s = [] 
block = 0

## Code Start
for i in range(len(a)):
    if a[i] == "(":
        s.append("(")
    
    else: # a[i] == ")"
        if a[i-1] == "(": #레이저인 경우
            s.pop()
            block += len(s)
        else:
            s.pop()
            block += 1
    
## Code End
print(block) 
