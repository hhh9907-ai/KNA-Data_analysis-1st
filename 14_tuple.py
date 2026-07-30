# tuple: 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 꼭 ,를 붙여야 python이 튜플로 인식을 함
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형이다

# sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = ("모터온도",78,)  # 괄호 있고, 끝에 쉼표 있음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = 78  # 괄호 없고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'int'>

# sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# # 요소 2개 이상: 쉼표가 있다면 튜플
# # 요소 1개 일때 : 쉼표 여부
# # 요소 0개(빈 튜플) : () 빈 괄호일때 튜플

# # 튜플에서 많이 헷갈려 하는 부분
# # (1) : int
# # (1,): tuple

# #(1,2,3,) -> 가장 마지막에 쉼표를 붙여서 튜플임을 명시

# # 튜플의 인덱스
# print sensor([0]) # 모터온도

# 튜플의 슬라이싱
# s = (
#     "a",
#     " b",
#     "c",
#     "d",
#     "e",
# )
# print(s[1:4])
# # 슬라이싱한 결과는 소괄호에 감싸져 있음
# # 튜플은 슬라이싱해도 튜플
# print(type(s[1:4]))

# # 튜플 언패킹
# # 튜플에 담긴 값을 변수로 한 번에 분리

# # 복습) 복수의 변수 한 번에 선언하기
# a, b, c = "a", "b", "c"
# print(a)
# print(b)
# print(c)

unpacking = (1, 2, 3)
# unpacking = one, two, three
# one, two, three라는 알 수 없는 변수를
# unpacking 변수에 할당하겠다는 의미
# 동작 x

one, two, three = unpacking
# unpacking이라는 변수에 담긴 튜플 내부의 값들을
# 할당 연산자 왼쪽 one, two, three 변수에
# 풀어서 담는다는 뜻
print("one", one)
print("two", two)
print("three", three)
