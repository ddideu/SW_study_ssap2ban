K = int(input())
for i in range(K):
    P, M = map(int,input().split())
    # B = []
    B = set() #여기까지는 일단 필요 왜냐면 각 테스트 케이스에 대한 K번 만큼 반복을 해야하니까.
    # C_count = 0

    for j in range(P):
        # A = int(input())
        # B.append(A)
        # # B.append(int(input))

        B.add(int(input())) #여기까지도 우선은 필요. 왜? 현재 B에대한 카운트를해야하니까 내가 생각하기에는.
    
    #이런식으로 처리를 해도 답이 나오는구나.
    C = list(set(B))
    print(P-len(C)) 

    # print(P-len(B))

    #원래 답.
    # for k in range(1, M+1):
    #     if B.count(k) >= 2:
    #         C_count += B.count(k) - 1
#아... 다중포문... 이거를 다중포문 없이 푸는 방법이 있을까? 
    
    # print(C_count)

    '''개인 의견 : 코드를 제출하고 다시 풀어보니 코드가 너무 길었던 감도 있고 해당 문제의 답에 다가가는 방법은
    많다라는것을 알게 됐다. 해당 문제를 푸는데 for문 낭비가 심했으며 해당 문제를 푼이후 다시 생각을 해보니 
    set을 이용한다면 더 쉽게 할수 있지 않았을까 라는 생각이 든다.'''