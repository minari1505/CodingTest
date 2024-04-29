#Memoization하기 위한 리스트 초기화
lst = [0] * 100

#피보나치 함수를 재귀로 구현(탑다운 DP)
def fibo(x):
    #종료조건 (1 or 2일 때 1을 반환)
    if x==1 or x==2:
        return 1
    #이미 계산한 적 있는 문제라면 그대로 반환
    if lst[x] != 0:
        return lst[x]
    #아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    lst[x] = fibo(x-1) + fibo(x-2)
    return lst[x]


print(fibo(99))