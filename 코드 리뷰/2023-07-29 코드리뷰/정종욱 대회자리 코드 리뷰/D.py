# BOJ_5176 : 대회 자리
import sys
input = sys.stdin.readline

test_num = int(input()) #확인해볼 test횟수 구하기

for _ in range(test_num): #test횟수 만큼 반복문
    P,M = map(int,input().split()) #사람수와 좌석수 입력 받고
    lst = [0 for _ in range(M)] #좌석수 만큼 list 만들기/ 각 index에 0값 추가
    for i in range(P):  # 사람 수만큼 반복문
        seat = int(input())  # 예약해놓은 좌석 번호 입력받기
        lst[seat-1] += 1   # 좌석 번호 - 1 = index값이므로 index 값에 1씩 더해줌
    
    count_list = [] #빈 list 만들기

    for j in range(len(lst)): #lst 항목의 개수만큼 반복
        if lst[j] > 1:  #lst가 1보다 크면 자리가 겹친다는 소리
            count_list.append(lst[j]-1) # 겹치는 자리에 1명은 앉을 수 있으니 -1
    print(sum(count_list[:M])) #count list에 추가한 값 모두 더하기

    '''의견 : 10번째줄의 for i in range(P)가 있을까요? 
    위쪽의 리스트 컴프리 핸션을 [int(input()) for _ in range(P)] 을 하시거나
    lst = [] 하고 그 밑을  for문 돌리면서 lst.append(int(input))을 하셨다면 더 깔끔하지 않았을까요?
    이유가 몇번 좌석을 앉으려고 했는지 입력을 하면서 아니까 이를 리스트에 추가하고 앉은 좌석별 언급 횟수에
    대한 for문을 안돌리셨어도 될것 같습니다.
    그리고 그다음 count_list를 리스트가 아닌 0으로 두고 if문의 조건식이 참일경우 count += lst[j] - 1
    을 하신후 print(count)를 하셨으면 좋았을것 같습니다.'''
