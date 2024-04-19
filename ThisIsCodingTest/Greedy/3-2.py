N,M,K = map(int,input().split())
N = list(map(int,input().split()))

#1. N을 내림차순 정렬
#2. N중 가장 큰 수, 두번째로 큰 수만 남기기
#3. N중 가장 큰 수를 최대 K번 더하고, 두번째로 큰 수 한 번 더하기를 M번만큼만 반복

ans = 0
#1. 
N.sort(reverse=True)

#2.
fst = N[0]
snd = N[1]

#3.
cnt = 0
cnt_K = 0
while cnt < M:
    cnt += 1
    
    if cnt_K != K:
        ans += fst
        cnt_K += 1
        
    elif cnt_K == K:
        ans += snd
        cnt_K = 0

print(ans)