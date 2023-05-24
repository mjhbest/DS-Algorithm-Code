def downup(w):
    print(w)
    if len(w) <= 1:
        return
    downup(w[:-1])
    print(w)


downup("Hello")


def factorial(n):
    if n == 1:
        return 1

    result = n * factorial(n-1)
    return result

# print(factorial(4))
