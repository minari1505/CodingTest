n,m = map(int,input().split())

lst = []
for i in range(n):
    lst.append(int(input()))

#계산결과 저장할 list
d = [10001] *(m+1)

#DP (bottom up)
d[0] = 0
for i in range(n):
    for j in range(lst[i], m+1):
        if d[j - lst[i]] != 10001: #(i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-lst[i]]+1)

#계산 결과 출력
if d[m] == 10001: #최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    pritn(d[m])