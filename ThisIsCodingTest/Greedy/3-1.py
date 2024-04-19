N = int(input())
cnt = 0

#큰 단위위 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    cnt += N // coin 
    N %= coin
    
print(cnt)