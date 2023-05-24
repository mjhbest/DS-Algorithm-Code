## [미션3-2] 하노이의 탑 ##
def move(no: int, x: int, y: int) -> None:
    """원반을 no개를 x 기둥에서 y 기둥으로 옮김"""
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')

    if no > 1:
        ## [미션] ##
        move(no-1, 6-x-y, y)


n = 4
print(f'원반의 개수: {n}')
move(n, 1, 3)
