from collections import deque

n,m = map(int,input().split())
maps = []
for i in range(n):
    maps.append(list(map(int,input())))

#이동할 네 방향(위왼아오)
nr = [-1,0,1,0]
nc = [0,-1,0,1]

#BFS
def bfs(r,c):
    #queue구현
    queue = deque()
    queue.append((r,c))
    #큐가 빌 때 까지 반복하기
    while queue:
        r, c = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nr = r + nr[i]
            nc = c + nc[i]
            #미로 공간을 벗어나면 x
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            #벽이면 x
            if maps[nr][nc] == 0:
                continue
            #해당 노드를 처음 방문하면 최단거리 기록
            if maps[nr][nc] == 1:
                maps[nr][nc] = maps[r][c]+1
                queue.append((nr,nc))
    #가장 오른쪽 아래까지의 최단거리 반환
    return maps[r-1][c-1]

#결과
print(bfs(0,0))