n,m = map(int,input().split())
result = 0
#한 줄씩 입력받아 확인하기
for i in range(n):
    data = list(map(int,input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_val = min(data)
    #가장 작은 수들 중 가장 큰 수 찾기
    result = max(result, min_val)

print(result)