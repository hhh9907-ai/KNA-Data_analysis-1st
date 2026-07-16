# print(3 + 5)
# print(10 - 4)
# print(3 * 8)
# print(10 / 4)
# print(10 // 4)
# print(10**4)
# print(80 % 5)

# a = 17
# b = 5
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a**b)

# x = 10
# y = 20
# z = 30
# print((x + y + z) / 3)

# # 정사각형 한변의 길이 : 10
# print(10 * 10)

# # 직사각형 변의 길이 가로 5 세로 10 높이 11
# print(5 * 10 * 11)

# print(7 < 16)
# print(7 > 16)
# print(7 <= 16)
# print(7 >= 16)
# print(7 == 16)
# print(7 != 16)

# print("hello" != "hello")  # False

# 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교
# print("=== 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교 ===")
# hello = hi
# print(hello == hi)  # NameError(선언하지 않은 이름 호출했을 때)
# hi는 따옴표에 감싸져있지 않기 때문에 변수로 취급됨
# 그런데 우리는 hi 변수를 선언한 적이 없기 때문에 에러

# 질문 1) 해결방법
# print("=== 질문 1) 해결 방법 ===")
hi = "안녕"  # hello 변수에 hi 변수를 할당하기 전 hi 변수 선언
hello = hi  # print(hello) > 안녕
print("=== 변수 hello(안녕)와 변수 hi(안녕) 비교 ===")
print(hello == hi)  # True
