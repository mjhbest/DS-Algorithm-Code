"""
input으로 N개의 웹사이트
action : ['back','front']

입력값 : N : 웹사이트 갯수
websites 입력값
action 순서 :  ['back','front','back','back]


<Detail>
1. 출력값 : 최종 도달한 웹사이트
2. back을 너무 많이하는 경우 : '불가능합니다' 출력
"""
N = 7
websites = ['youtube.com', 'naver.com', 'google.com',
            'elice.io', 'daum.net', 'google.com', 'youtube.com']
# actions = ['back','front','back','back','back','front','back']
actions = ['back', 'front', 'front']

# Codes
# 1. Stack 구성
prev_stack = []
next_stack = []
error_flag = False

for website in websites:
    prev_stack.append(website)

print("prev : ", prev_stack)
print("next : ", next_stack)
print("curr : ", prev_stack[-1])

# 2. action 진행
for action in actions:
    if action == 'back':
        if len(prev_stack) == 0:
            error_flag = True
            break

        curr = prev_stack.pop()
        next_stack.append(curr)

    else:
        if len(next_stack) == 0:
            error_flag = True
            break

        prev_stack.append(next_stack.pop())

print()
# 3. 현재 페이지 확인
print("prev : ", prev_stack)
print("next : ", next_stack)
print("curr : ", prev_stack[-1])
if not error_flag:
    print(prev_stack[-1])
else:
    print("불가능합니다.")
