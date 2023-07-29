import sys

n_cases = int(sys.stdin.readline())
answers = [] 

for _ in range(n_cases):
    n_participants, n_seats = map(int, sys.stdin.readline().split())
    seats = []
    for _ in range(n_participants):
        seats.append(int(sys.stdin.readline()))

    seats_set = set(seats)
    len_seats_in_use = len(seats_set)
    
    answers.append(n_participants - len_seats_in_use)

for answer in answers:
    print(answer)

    '''개인 의견: 역시 갓 하지만 내가 생각하기에는 4번 라인의 각 테스트 케이스에 대해서 출력을 하라고 했으니 
    굳이 이것을 쓰지 않았어도 되지 않았을까? 라는 생각이 들었고 그렇게 되면 15번 라인의 
    append를 하지않고 바로 print(n_participants - len_seats_in_use) 해도 됐을것 같다. 그렇다면 그밑의
     17번 라인 밑으로는 지워도 됐을것 같다라는 생각이 든다. '''