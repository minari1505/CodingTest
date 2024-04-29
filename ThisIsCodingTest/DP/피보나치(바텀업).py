#앞서 계산된 결과를 저장하기 위한 list
lst = [0] * 100

#첫번째 피보나치 수와 두번째 피보나치 수는 1
lst[1] = 1
lst[2] = 1
n = 99

#피보나치함수를 반복문으로 구현
for i in range(3, n+1):
    lst[i] = lst[i-1] + lst[i-2]

print(lst[n])
