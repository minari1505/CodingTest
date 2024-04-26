n,m = map(int,input().split())
height = list(map(int,input().split()))

start = 0
end = max(height)

cnt = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in height:
        #잘랐을 때 떡의 양 계산하기
        if i > mid:
            total += i - mid
    #떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 탐색)
    if total < m:
        end = mid - 1
    #떡의 양이 충분한 경우 덜 자르기(오른쪽 탐색)
    else:
        result = mid #최대한 덜 잘랐을 때가 정답, result에 기록해두기
        start = mid + 1

print(result)