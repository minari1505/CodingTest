#각 부품이 존재하면 yes, 없으면 no 출력하기
n = int(input())
array = list(map(int,input().split()))
m = int(input())
m_lst = list(map(int,input().split()))

#1. n개의 부품을 번호 기준으로 정렬하기
array.sort()

#2. 이진탐색 소스코드(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        #찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        #중간점의 값보다 찾고자 하는 값이 작을 때 왼쪽 확인
        elif array[mid] > target:
            end = mid -1
        #중간점의 값보다 찾고자 하는 값이 클 때 오른쪽 확인
        elif array[mid] < target:
            start = mid + 1
    return None

#3. 손님이 확인 요청한 부품 번호 확인하기
for i in m_lst:
    #해당 부품이 존재하는지 확인
    cnt = binary_search(array, i, 0, n-1)
    if cnt != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

