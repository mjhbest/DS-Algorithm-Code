def changes(coins,money,price):
    """
        물건 값을 입력하면 '잔돈갯수' 만을 출력
        받은 잔돈의 종류와 종류별 잔돈갯수를 출력하기 위한 코드

        입력값:
            100
        출력값:
            {700: 1, 100: 2}
    """
    change = money - price # 900
    result = {}

    for coin in coins: # 700, 400, 300, 100, 50, 10
        if change < coin:
            continue
        result[coin] = change//coin # 주어야 하는 코인의 갯수
        change -= coin * (change//coin) #잔돈 차감
    
    return result
    
money = 6000
price = 3400
coin_list = [700, 400, 300, 100, 50, 10] # 각 동전의 갯수제한X
print(changes(coin_list,money,price))
