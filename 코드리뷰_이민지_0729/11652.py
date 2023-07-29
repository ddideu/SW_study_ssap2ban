# 문제 처리 조건 
# 가장 많이 가지고 있는 카드를 구해라
# 카드 개수가 똑같으면 작은수를 출력해라
import sys
n = int(sys.stdin.readline())
card_dict = {}
for i in range(n):
    card =int(sys.stdin.readline())
    if card in card_dict:
       card_dict[card] += 1
    else:
        card_dict[card] = 1
print(card_dict)
# result ={}
# #value값기준 key 값 정렬
# # A: 
# result = sorted(card_dict.items(), key = lambda x:x[1], reverse=True)
# B
result = sorted(card_dict.items(),key = lambda x : (-x[1],x[0]))

print(result)
print(result[0][0])