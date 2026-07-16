# input- 사용자 입력

# input("이름 : ")
# input("성별 : ")

# name = input("이름(변수 할당 ver): ")
# age = input("나이(변수 할당ver): ")

# print("입력 받을 이름은", name, "입니다. ")
# print("입력 받을 나이는", age, "입니다. ")

# name = input("이름")
# print("안녕하세요" + name + "님!")


# age = int(input("나이 : "))
# print(age + 5)


# birthday_year = int(input("태어난 연도"))

# age = 2026 - birthday_year

# print("당신의 나이는" + str(age) + "살 입니다!")


# tall = float(input("당신의 키는? "))
# print("당신의 키는", tall, "난쟁이 똥자루 입니다")


# nation = input("당신이 거주하는 국가는: ")
# city = input("당신이 거주하는 도시는: ")

# print("당신이 거주지는", str(nation) + "의", city, "입니다!")

# a = int(input("당신의 선택한 숫자"))
# b = int(input("당신이 선택한 두번째 숫자"))

# print("더하기: ", a + b)
# print("빼기: ", a - b)

# temp = int(input("출력 온도 작성하시오"))

# print(temp > 80, temp >= 0)


a = int(input("당신의 국어 점수는? "))
b = int(input("당신의 영어 점수는? "))
c = int(input("당신의 수학 점수는? "))

avg = (a + b + c) / 3
print("당신의 평균 값은 60점 이상인가요?", avg > 60)
