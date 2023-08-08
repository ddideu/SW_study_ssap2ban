S = int(input())
for i in range(S):
    T_sum = 2015
    T = set(map(str,input()))
    for i in T:
        T_sum -= ord(i)
    print(T_sum)
