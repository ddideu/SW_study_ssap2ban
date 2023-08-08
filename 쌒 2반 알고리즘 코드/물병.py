N, K = map(int,input().split())
if N < K:
    print(0)   
else:        
    for j in range(K):
        i = 1
        while N > i :
            i *= 2 
        if j != K-1 :
            if N - i < 0:
                N -= i/2
            else:
                N -= i
                if N == 0:
                    print(0)
                    break
        else:
            N -= i
            A = abs(N)
            print(int(A))

# if B[K-1] >= 0:
#     print(0)
# else:
#     C = B[K-1]
#     D = abs(C)
#     print(int(D))


        
