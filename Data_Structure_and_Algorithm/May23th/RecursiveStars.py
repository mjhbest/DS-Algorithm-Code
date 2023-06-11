def make_stars(n: int) -> list:
    # 종료 조건
    if n == 1:
        return ['*']

    # Recursive Works
    sub_stars = make_stars(n//3)
    output = []

    # 맨 윗줄
    for sub_star in sub_stars:
        output.append(sub_star*3)

    # 두번째 줄 4~6
    for sub_star in sub_stars:
        output.append(sub_star + ' '*(n//3) + sub_star)

    # 세번째 줄 7~9
    for sub_star in sub_stars:
        output.append(sub_star*3)

    return output


N = 27
print('\n'.join(make_stars(N)))


#####
# Example

# N = 3
# ***
# * *
# ***

# N = 9
# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
# *********
# * ** ** *
# *********
