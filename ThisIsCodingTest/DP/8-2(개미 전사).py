n = int(input())

#모든 식량 정보 입력받기
k = list(map(int, input().split()))

#앞서 계산된 결과 저장할 list
lst = [0] * 100

#DP 진행 (bottom up)
lst[0] = k[0]
lst[1] = max(k[0], k[1])
for i in range(2, n):
    lst[i] = max(lst[i-1], lst[i-2]+k[i])

print(lst[n-1])