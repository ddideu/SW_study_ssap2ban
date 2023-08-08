import sys

N, M = map(int,sys.stdin.readline().split())
A = []
B = []
C_count = 0
for i in range(N+M):
    if i <= N-1:
        A.append(str(sys.stdin.readline()))
    else:
        B.append(str(sys.stdin.readline()))

for i in A:
    C_count += B.count(i)
    
print(C_count)