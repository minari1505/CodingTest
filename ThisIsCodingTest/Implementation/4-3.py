#1. 현재 위치 저장
#2. 나이트의 이동방향 저장하기
#3. 이동방향 (최대 8번) 이동시켜보고, 벽에 막혔다면 continue
#4. 이동이 가능할 때에만 cnt += 1
direc = input()
cnt = 0
row_dict = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8}

#1.
r, c = row_dict[direc[0]], int(direc[1])

#2.
nr = [2, 2, 1, 1, -2, -2, -1, -1]
nc = [1, -1, 2, -2, 1, -1, 2, -2]

#3.
for i in range(8):
    nnr = r + nr[i]
    nnc = c + nc[i]
    #이동하지 못하는 경우
    if nnr < 1 or nnr > 8 or nnc < 1 or nnc > 8:
        continue
    cnt += 1

print(cnt)