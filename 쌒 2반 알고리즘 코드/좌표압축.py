import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = list(set(A)) 
B.sort()
A_dict = {}

#딕셔너리 없이 풀고는 싶었지만 풀수가 없었다. 아니 푸는 방법은 존재 했지만 시간 초과가 났다.
#이 문제를 풀면서 확실하게 딕셔너리쪽을 잡고 가는것이 마음이 편할것 같다.
for i in range(len(B)):
    A_dict[B[i]] = i

C = []
for i in A:
    C.append(A_dict[i])
print(*C)

# 해당 코드가 내가 제일 처음으로 생각해냇던 코드이다.
# B = A[:]
# C = list(set(B)) 
# C.sort()
# K = 0

# for i in C:
#     for j in range(len(A)):
#         if i == A[j]:
#             A.remove(i)
#             A.insert(j, K)
#     K += 1   

# print(*A)
       

    
