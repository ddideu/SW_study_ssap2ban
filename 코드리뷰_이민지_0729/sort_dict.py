# 1 sorted 함수로 dic을 정렬하면 어떻게 될까? 

dic = {'e' : 2, 'a': 3, 'b':1, 'c' : 4, 'd' : 5}
dic = sorted(dic)
print(dic)


# 2 key 값을  내림차순 하고 싶다면?
# dic = {'e' : 2, 'a': 3, 'b':1, 'c' : 4, 'd' : 5}
# dic = sorted(dic, reverse= True)
# print(dic)

# # # 3 key 값을 기준으로 오름차순 but value값도 반환해줘
# dic = {'e' : 2, 'a': 3, 'b':1, 'c' : 4, 'd' : 5}
# dic = sorted(dic.items())
# print(dic)

# # # 4 key 값을 기준으로 내림차순 but value값도 반환해줘
# dic = {'e' : 2, 'a': 3, 'b':1, 'c' : 4, 'd' : 5}
# dic = sorted(dic.items(), reverse = True)
# print(dic)

# ## 5 먼저 이해 해야 할 것 딕셔너리를 정렬하고 프린트했을때
# ## 튜플 형식으로 반환 
 
# # # 6 Value 값 기준으로 정렬하고 싶어 ! 어떻게 해야할까?
# dic = {'e' : 2, 'a': 3, 'b':1, 'c' : 4, 'd' : 5}


# # # 7key 값을 설정하면 된다 어떻게? lambda로 
# dic = sorted(dic.items(), key = lambda x : -x[1])
# # x[0]은 Key , x[1]은 value 
# print(dic)

# 8 위의 방법이 좋은 점이 뭘까? 정렬 기준이 여러개일때 좋다
# 9 정렬 우선 순위를 지정할 수 있다 

# 10 example : value를 오름차순 후 key 오름차순 

# dic = {'e' : 1, 'a': 3, 'b':1, 'c' : 4, 'd' : 5}
# # dic = sorted(dic.items(), key = lambda x :x[1])
# dic = sorted(dic.items(), key = lambda x :(x[1],x[0]))
# # print(dic)

# ## 11 key의 길이도 정렬 기준으로 만들 수 있다. 어떻게? 20920문제

# # # 12 value 내림차순은 정렬기준에 -를 붙이면 된다. 
# dic = {'e' : 1, 'a': 3, 'b':1, 'c' : 4, 'd' : 5}
# dic = sorted(dic.items(), key = lambda x : -x[1])
# print(dic)



# # # 13 이 표현식(-)의 한계점 key를 내림 차순 하고 싶을때는 안됨
 
# dic = {'e' : 1, 'a': 3, 'b':1, 'c' : 4, 'd' : 5}
# dic = sorted(dic.items(), key = lambda x : -x[0])
# print(dic)

# # ## 14 그럼 여기서 문제 value를 오름차순 후 키 값을 내림 차순 하고 싶으면?
# dic = sorted(dic.items(), key = lambda x : (x[1],-x[0]))
# 오류난다 왜? key가 문자열

# #15 일단 value 오름차순 한 상태 보기 
# dic = {'e' : 1, 'a': 3, 'b':1, 'c' : 1, 'd' : 5}
# dic = sorted(dic.items(), key = lambda x : x[1])
# print(dic)


# # ## 16 문자열을 아스키 코드로 변환 그럼 숫자니까 정렬되지 않나?
# # ## 문자열 -> 숫자 함수 ord 접목
# dic = sorted(dic.items(), key = lambda x : (x[1],-ord(x[0]))) 
# print(dic)
