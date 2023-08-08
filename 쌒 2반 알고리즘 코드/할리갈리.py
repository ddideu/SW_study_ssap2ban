import sys

A = int(sys.stdin.readline())
A_Count = 0
B_Count = 0
C_Count = 0
D_Count = 0
bell = 1
#STRAWBERRY, BANANA, LIME, PLUM
for i in range(A):
    S, X = map(str,sys.stdin.readline().split())
    if S == 'STRAWBERRY':
        A_Count += int(X) 
    if S == 'BANANA':
        B_Count += int(X)
    if S == 'LIME':
        C_Count += int(X)
    if S == 'PLUM':
        D_Count += int(X)

Max_count = [A_Count, B_Count, C_Count ,D_Count]
for i in Max_count:
    if i == 5:
        bell = 0
        break

if bell == 0:
    print('YES')
else:
    print('NO')