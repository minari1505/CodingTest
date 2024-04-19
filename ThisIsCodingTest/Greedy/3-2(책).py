#N : 배열의 크기
#M : 숫자가 더해지는 횟수
#K : 반복 가능한 최대 횟수
N,M,K = map(int,input().split())
data = list(map(int,input().split()))

data.sort(reverse=True)
fst = data[0]
snd = data[1]

result = 0

while True:
    for i in range(K): #가장 큰 수를 K번 더하기
        if M == 0: #m이 0이면 반복문 탈출
            break
        result += fst
        M -= 1 #더할 때 마다 1씩 빼기
    if M == 0: #m이 0이라면 반복문 탈출
        break
    result += snd #두 번째로 큰 수를 한 번 더하기
    M -= 1 #더할 때 마다 1씩 빼기

print(result)