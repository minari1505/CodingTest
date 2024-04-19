#얼음 틀 모양이 주어졌을 때 생성되는 총 아이스크림의 개수
#DFS

n,m = map(int,input().split())
maps = []
for i in range(n):
    maps.append(list(map(int,input())))

#dfs로 특정 노드 방문 시 이어진 노드들 방문
def dfs(r,c):
    #주어진 범위를 벗어나면 종료
    if r <= -1 or r >= n or c <= -1 or c >= m:
        return False
    #현재 노드를 방문하지 않았다면
    if maps[r][c] == 0:
        #해당노드 방문처리하기
        maps[r][c] = 1
        #상하좌우 재귀호출
        dfs(r-1,c)
        dfs(r,c-1)
        dfs(r+1,c)
        dfs(r,c+1)
        return True
    return False

#모든 위치에서 음료수 채우기
ans = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 수행하기
        if dfs(i, j) == True:
            ans += 1
print(ans)