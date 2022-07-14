coins = [500, 100, 50, 10, 5, 1]

payMoney = int(input())
change = 1000 - payMoney
moneyCount = 0

for coin in coins:
    if change >= coin:
        moneyCount += change // coin
        change %= coin
    
print(moneyCount)