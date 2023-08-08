import sys

N, K = map(int,sys.stdin.readline().split())
coin = [] 
coin_count = 0
for i in range(N):
    coin.append(int(sys.stdin.readline()))

coin.sort(reverse = True)
for i in coin:
    if K // i != 0:
        coin_count += K//i
        K -= (K//i)*i
        if K == 0:
            print(coin_count)
            break
