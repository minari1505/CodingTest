#큰 수에서 작은 수의 순서로 정렬

#1. 선택 정렬
n = int(input())
lst = list()
for i in range(n):
    lst.append(int(input()))

for i in range(len(lst)):
    #가장 작은 원소의 인덱스
    min_i = i
    for j in range(i+1, len(lst)):
        if lst[min_i] > lst[j]:
            min_i = j
    lst[i], lst[min_i] = lst[min_i], lst[i]

print(lst.reverse())

#2. 삽입 정렬
n = int(input())
lst = list()
for i in range(n):
    lst.append(int(input()))

for i in range(1, len(lst)):
    for j in range(i, 0, -1):
        if lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
        else:
            break

print(sorted(lst, reverse=True))

#3. 퀵 정렬
n = int(input())
lst = list()
for i in range(n):
    lst.append(int(input()))

def quick_sort(lst):
    #리스트가 하나이하의 원소만 있다면 종료
    if len(lst) <= 1:
        return lst

    pivot = lst[0] #첫번째 원소 = 피벗
    tail = lst[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    rev_ans =  quick_sort(left_side) + [pivot] + quick_sort(right_side)
    rev_ans.sort(reverse=True)
    return rev_ans

print(quick_sort(lst))

#4. 계수 정렬
n = int(input())
lst = list()
for i in range(n):
    lst.append(int(input()))

count = [0] * (max(lst)+1)

for i in range(len(lst)):
    count[lst[i]] += 1

for i in range(len(count),0,-1):
    for j in range(count[i]):
        print(i, end=' ') #띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력하기