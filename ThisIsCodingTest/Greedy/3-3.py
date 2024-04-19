#1. 0행의 가장 낮은 숫자를 변수에 저장함
#2. cards 각 행을 오름차순 정렬
#3. 그 다음 행의 가장 낮은 숫자가 저장된 변수보다 크다면, 변수를 변경
n,m = map(int,input().split())
cards = [list(map(int,input().split())) for _ in range(n)]

#1.
ans = min(cards[0])

#2.
for i in range(1, len(cards)):
    cards[i] = sorted(cards[i])
    if ans < cards[i][0]:
        ans = cards[i][0]
    else:
        pass

print(ans)