# 입력값 설정
# N = int(input())
N = 2
sentences = ['I am happy today', 'We want to win the first prize']


# append(), pop()
# 알고리즘 풀이
# Solution 1 - indexing
print("Solution 1")
for i in range(N):
    # input_string = input()
    input_string = sentences[i]

    # Code
    stack = []
    for c in input_string:
        if c == " ":
            while len(stack) != 0:
                print(stack.pop(), end='')
            print(' ', end='')

        else:
            stack.append(c)

    while len(stack) != 0:
        print(stack.pop(), end='')
    print(' ', end='')

    print()


# Solution 2 - Split
print()
print("Solution 2")
for i in range(N):
    # input_string = input()
    input_string = sentences[i]

    # Code
    stack = []
    words = input_string.split()
    for word in words:
        for c in word:
            stack.append(c)

        while len(stack) != 0:
            print(stack.pop(), end='')
        print(' ', end='')

    print()


# Solution 3 - Without Stack Concept
print()
print("Solution 3")
for i in range(N):
    # input_string = input()
    input_string = sentences[i]

    # Code
    words = input_string.split()
    for word in words:
        print(''.join(reversed(word)), end=' ')
    print()


# Solution 4 -
print()
print("Solution 4")
for i in range(N):
    # input_string = input()
    input_string = sentences[i]

    # Code
    words = input_string.split()

    for word in words:
        print(word[::-1], end=' ')
    print()
