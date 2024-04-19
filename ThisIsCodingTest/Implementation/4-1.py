n = int(input())
moves = list(map(str,input().split()))

r, c = 1, 1 #시작 위치의 r, c값 저장

nr = [-1, 0, 1, 0] #URDL
nc = [0, 1, 0, -1]
move_direc = ["U", "R", "D", "L"]

for move in moves:
    for i in range(4): #4방향 모두 확인
        if move == move_direc[i]:
            nnr = r + nr[i]
            nnc = c + nc[i]
    if nnr < 1 or nnr > n or nnc < 1 or nnc > n:
        continue
    r, c = nnr, nnc

print(r, c)
       