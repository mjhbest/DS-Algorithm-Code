num = input()
numbers = list(map(int,input()))

s = 0
for number in numbers:
    s += number
print(s)

print(sum(numbers))
