# 영어 암기는 괴로워 20920
# https://www.acmicpc.net/problem/20920
# 문제 요구 조건 
# 자주나오는 단어 -> 길이가 긴 단어 -> 알파벳 사전순 앞에있는 단어

# 단어개수 N , 외울 길이 M 이상
import sys
input = sys.stdin.readline
# 단어개수 N , 외울 길이 M 이상
n, m = map(int, input().split())
word = []   # 입력받는 단어를 저장할 리스트 생성
memory = dict()
for i in range(n):
    w = input().rstrip()
    if len(w)>=m:      # 단어의 길이가 m 이상일 때 만 
        word.append(w)  # 리스트에 저장

for wo in word:  # 리스트에 있는 단어(요소)를 하나씩 검사
    memory.setdefault(wo,0) # 딕셔너리로 빈도수 저장 
    memory[wo] += 1

# memory 딕셔너리 출력으로 빈도수 확인 
print(memory)     
result = sorted(memory.items(), key = lambda x: (-x[1],-len(x[0]),x[0]))

for i in result:
    print(i[0])