#1.
from collections import defaultdict
n = int(input())

dct = defaultdict(list)
for i in range(n):
    a, b = input().split()
    dct[a].append(b)

sorted_dct = sorted(dct.items(), key = lambda item:item[1])

for student in sorted_dct:
    print(student[0], end = ' ')

#2.
n = int(input())

lst = []
for _ in range(n):
    input_data = input().split()
    lst.append((input_data[0], int(input_data[1])))

lst = sorted(lst, key=lambda item: item[1])

for student in lst:
    print(student[0], end= ' ')