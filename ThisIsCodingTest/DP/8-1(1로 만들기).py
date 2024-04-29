#정수 x 입력받기
x = int(input())

#앞서 계산된 결과를 저장하기 위한 리스트
lst = [0] * 30001

#DP 진행(bottom up)
for i in range(2, x+1):
    #현재의 수에서 1을 빼는 경우
    lst[i] = lst[i-1] + 1

    #현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        lst[i] = min(lst[i], lst[i//2]+1)
    
    #현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        lst[i] = min(lst[i], lst[i//3]+1)
    
    #현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        lst[i] = min(lst[i], lst[i//5]+1)

print(lst[x])