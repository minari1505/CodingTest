n = int(input())

#앞서 계산된 결과 저장할 list
lst = [0] * 1001

#DP (bottom up)
lst[1] = 1
lst[2] = 3
for i in range(3, n+1):
    lst[i] = (lst[i-1] + 2*lst[i-2])%796796

print(lst[n])