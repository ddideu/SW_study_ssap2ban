import sys
sys.stdin = open('import.txt') 
# #아마 틀린 이유가 이것때문이지 않을까 조심스럽게 생각해봅니다.
#input = sys.stdin.readline

x = int(input())

for i in range(x):
    P_wants = []
    count = 0
    P, M = map(int, input().split())
    for i in range(P):
        P_wants.append(int(input()))

    if M == 1: # 자리가 한개일때
        print(P - 1)  
    else:
        count = 0
        for i in range(1, M+1):
            if P_wants.count(i) >= 2:      # 동일 자리가 2개 이상일때
                count += P_wants.count(i) - 1
        print(count)
#정상 작동이 되야 하는데 아마도 백준에서 txt 파일을 못받은것 같습니다.
'''개인의견: 한번 txt파일을 빼고 다시 돌려보세요. 아마 돌아갈듯 싶습니다.'''