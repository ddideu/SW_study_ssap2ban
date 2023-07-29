import sys
input = sys.stdin.readline

K = int(input())  # 테스트 케이스 개수

for i in range(K):  # 테스트 케이스 개수만큼 반복한다
    P, M = map(int, input().split())  # 참가자 수 P, 자리의 수 M 입력

    if 1 <= P and P <= 500 and 1 <= M and M <= 500:
        line = [int(input()) for _ in range(P)]  # P(참가자 수)개 줄에 원하는 자리번호들 입력
        remaining_line = list(set(line)) # set으로 중복 제거해서 line에 중복된 번호를 가진 참가자들을 제외한 남은 참가자들을 구함
        unable_to_seat = P - len(remaining_line) # 자리에 앉을 수 없는 사람들의 수를 구함
    
    print(unable_to_seat)
    
    '''개인 의견: 해당 문제에 대한 이해도가 높은 사람으로 생각합니다. 개인 생각을 뭔가 말할 이유가 없어 보이고
    굳이굳이 한다면 remaining_line = list(set(line)) 에서 리스트로 받지 않고 그냥 set으로 둬도 len함수가 숫자로 
    출력 돼서 위의 코드와 같은 답이 됩니다.'''

