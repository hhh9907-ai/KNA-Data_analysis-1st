# # 여러줄 문자열

# # notice = """설비 점검 안내
# # 1. 전원 확인
# # 2. 센서 점검"""

# # print(notice)


# # notice = "설비 점검 안내 \n1. 전원 확인\n2. 센서 점검"
# # print(notice)

# # tap = "이름/상태"
# # print(tap) #이름\상태 > 첫 번째 \는 이스케이프 문자라는 것을 알리는 용도

# # set = "PUMP_A"
# # status = "정상"
# # oper = 1200
# # view = "2026-07-16"

# # set_up = (
# #     "설비: " + set + "\n상태: " + status + "\n가동: " + str(oper) + "\n점검: " + view
# # )

# # print(set_up)

# # # ==================================================
# # word = "PHYTON"
# # print(word[0], word[5], word[3])

# # abc = "abcdefghijklnmopqrstuvwxyz"
# # # print(
# # #     abc[7]
# # #     + abc[0]
# # #     + abc[12]
# # #     + abc[7]
# # #     + abc[-2]
# # #     + abc[4]
# # #     + abc[14]
# # #     + abc[12]
# # #     + abc[6]
# # #     + abc[7]
# # #     + abc[4]
# # #     + abc[4]


# # print(abc[::-3])


# # start = "temp_sensor"
# # print(start[5:])


# # word = "sensor_01"
# # print(word[-2:])


# # word = "PHTYON"
# # print(word[::-1])

# # =============================================
# # 문자열의 길이 반환
# # print(len("hello world"))
# # print(len(" "))

# # var = "여러분 한시간 만 더 하면 됩니다 조금만 힘내세요!"
# # print(len(var))

# # num = "01012345678"
# # print(len(num))

# # text = "a,b,c,d"
# # print(text.count(","))

# # print("hong@company.com".find("@"))

# email = "hong@company.com"
# at = email.find("@")
# user_id = email[:at]
# print(user_id)

# tartswith()
# # 특정 문자열로 시작하는지 검사 후 True/False (bool)

# print("E200-008".startswith("E200"))

# # 변수 활용
# e200 = "E200"
# print("E200-008".startswith(e200)) # 변수명은 따옴표로 감싸면 안된다.!!!!!!!!!!

# # ======================================================================

# # endswith()
# # 특정 문자열로 끝나는지 확인
# # True / False로 반환

# str2 = "월요일입니다! 여러분은 할 수 있어요!"

# print(str2.endswith("!")) # True
# print(str2.endswith("요!")) # True
# print(str2.endswith("음")) # False
# print(str2.endswith(" 월요일입니다! 여러분은 할 수 있어요!")) # False
# print(str2.endswith("월요일입니다! 여러분은 할 수 있어요!")) # True
# print(str2.endswith("월요일입니다!   여러분은 할 수 있어요!")) # False

# # ===============================================================

# hsg = "sensor_log.csv"
# print(hsg.startswith("sensor"))
# print(hsg.endswith(".csv"))

# # ===============================================================

# print(type("잊어먹으면 안돼")) # class 'str'
# print(len("이렇게 썼죠")) # 6
# # endswith와 len의 차이점
# # endswith는 .으로 연결
#   # .으로 연결하는 이런 도구들은 "메서드"
#   # 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능
# # len은 . 사용 안함
#   # () -> GKATN
#   # LEN과 같이 개발자가 직접 선언하지 않은 기본 제공 함수 : 내장함수

# "str".startswith("s")
# # 123.startswith(1)
# # .으로 사용하는 메서드들은 특정 자료형(객체)마다 다르다
# # int 자료형의 객체에는 startswith라는 메서드가 없다

# # print(len(123)) -> Error

# # ==============================================================

# # 메서드 - 특정 자료형(값=객체)에 소속된 함수
# # 문자열.메서드이름()
# # 추가 정보가 필요하면 괄호 안에 인자 (count('a'))
# # 인자 없으면 괄호만 비워 둠
# # word = "python"
# # print(word.upper()) # python
# # print(word.count("p")) # 1
# # print(word.startswinth("p")) # True

# # ===============================================================

# num = 1
# num = num + 1 # 2
# num += 1 # 3
# # += 복합할당연사자로 원래 내 자신의 값에 다음 오는 연산자와 값을 적용해서 재할당

# # ====================================================================

# # .upper() - 영문 글자를  모두 대문자로

# str3 = "abcdefg"
# print(str3) # abcdefg

# str.upper # ABCDEFG -> 반환은 대문자인데, 값에 재할당은 x
# print(str3) # abcdefg -> 기존 str3의 값인 소문자를 그대로 출력

# # 앞으로 계속 대문자로 변환한 값을 사용하고 싶다면
# # 변수에 재할당을 해야함
# # 변수 재할당에서 변수 스스로를 부르는 것이 가능
# # 재할당에서 변수 스스로 값을 부르려면 "재할당" 이어야 한다

# str3 = str3.upper()

# # 최초 변수 할당 시에는 저장된 값이 없어서 변수 스스로 할당 불가능

# aug = "babo"
# bobo = aug.upper()
# print(bobo)

# # lower() - 영문 글자를 모두 소문자로

# a = "Warning"
# b = a.lower()
# print(b)

# # capitalize - 문장 철 글자만("python is" > "Pythom is")
# # title - 단어 마다 첫 글자("hong gil" > "Hong Gil")

# user_name = "kim chul su"
# print(user_name.capitalize()) # Kim chul su
# print(user_name.title()) # Kim Chul Su

# # '를 사용한 경우
# print("i'm full".title) # I'M Full

# # isupper - islower()
# print("ABC".isupper())
# print("abc".islower())
# print("Abc".islower())

# fama = "Sensor_LOG.CSV"
# mama = fama.lower()
# print(mama.startswith("sensor"))
# print(mama.endswith(".csv"))

# # ===========================================

# # .strip () - 문자열의 앞뒤 공배을 떼어 줌
# # .lstrip() - 왼쪽 공백만 제거
# # .rstrip() - 오른쪽 공백만 제거

# raw = "   정상    "
# print(raw.strip()) # 정상
# print(raw.lstrip()) # "정상    "
# print(raw.rstrip()) # "    정상"

# print("    정   상    ".strip) #   정    상

# print(raw)  #  "   정    상    "
#   # strip은 재할당이나 새 변수에 할당하지 않는 이상 휘발

# # strip으로 문자 제거
# str4 = "===정상==="
# print(str4.strip("=")) # 정상
# # 인자로 전달한 양 끝의 =이 모두 지워짐

# str5 = "=정상====="
# print(str5.strip("=")) # 정상
# # 갯수 상관 없이 인자로 전달한 문자를 무조건 삭제
# print(str5.strip("= ")) # 정상
# # strip 자체가 공백을 지우는 것이기 떄문에 공백 상관없이 양 끝의 해당 문자열 삭제

# str6 = "==정==상===="
# print(str6.strip("=")) # 정==상
# # 글자 중간에 있는 문자열은 건드리지 않는다

# # strip으로 못 지우는 중간 공백을
# # replace로 해결!!!!!!!!!!!!

# # ===================================================

# # 체이닝 x
# raw = "    NORMAL    "
# step1 = raw.strip() # NORMAL
# step2 = step1.lower() # normal

# # 체이닝 x, 기존 변수에 재할당
# raw = raw.strip() # NORMAL
# raw = raw.lower() # normal

# # 체이닝 o
# chain = raw.strip().lower() # normal

# # 기존 변수에 재할당도 가능
# raw = raw.strip().lower() # normal

# # 변수에 할당하지 않고 사용 가능
# print(raw.strip().lower()) # normal

# phone = "   Warning   "
# iphone = phone.lower()
# print("[" + iphone + "]")
# iphone = phone.strip().lower()
# print("[" + iphone + "]")

# # strip() 메서드에 인자로 들어가는 문자열은 완전히 동일하지 않아도 전부 삭제

# str7 = "aaab 이렇게? cd"
# print(str7.strip("abcd")) # " 이렇게?""
# print(str7.strip("abcd ")) # "이렇게?"
# print(str7.strip("bc")) # "aabb 이렇게? cd"
# print(str7.strip("ab")) # " 이렇게? cd"

# # GPT한테 질문을 하면서 이해를 하는법
# str7 = "aaab 이렇게? cd"
# print(str7.strip("abcd")) # " 이렇게? "

# # 지금 출력 결과는 " 이렇게? " 나오고 있어
# # 내가 생각했을 떄 == 처럼 정확하게 "abcd" 순서가 아니면
# # strip이 안될 줄 알았는데 실행 결과를 보니 순서랑 상관없이
# # 인자로 전달한 문자열에 해당하는 글자가 확인하는 문자열 양 끝에
# # 하나라도 있으면 동작하는 것 같아.
# # 내가 이해한게 맞아 ?
# # 그러면 왜 이렇게 동작하는거야 ?

# # =================================================================

# # replace() - 특정 글자, 단어를 다른 것으로 바꾸기
# # replace(" ","") -> 중간 공백 제거
# # "010-1234-1234".replace("-","")
# # text = "정 상 가 동"
# # text = text.replace(" ","") # 공백제거
# # print(text) # 정상가동
# # 체이닝으로 연계도 가능 !
# # "fault""FAULT"를 모두 "고장"으로 통일
# # "3,000"의 쉼표를 제거해 int로 변환 가능

# print(" 정 상 가 동".replace(" ","")) # 정상가동 -> 모든 공백 제거 !
# print("  정     상 가 동".replace("  ","")) # 정 상 가 동 -> 공백이 두칸 붙어있는 경우만 제거

# # 글자 치환
# print("고장".replace("고장", "fault")) # fault
# print("고장".replace("고", "fault")) # fault장

# # replace() 문자열 단어 치환
# str8 = "설비 정상 가동"
# print(str8.replace("정상", "점검")) # 설비 점검 가동

# # replace() 체이닝
# num = "    010-1234-1234    "
# print(num.replace(" ","").replace("-","")) # 01012341234

# # ===========================================================

# # 리스트 - 여러 값을 순서대로 담는 그릇
# # 대괄호 안에 값들을 쉼표로 나열 (사과,배,감) -> 사과 = 0 , 배 = 1, 감 = 2
# # 번호로 조각 하나를 꺼냄(0부터,문자열과 동일)
# # 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

# # split() - 정해진 구분자로 문자열을 여러 조각으로 나누기
# # 슬라이싱은 위치로 자르기, split은 구분자로 나누기
# "에스프레소 아메리카노 카페라떼".split()
# drinks = "에스프레소 아메리카노 카페라떼" # ["에스프레소", "아메리카노", "카페라떼"]
# print(drinks.split())
#   # 띄어쓰기를 기준으로 나뉘어진 세 개의 문자열을 대괄호에 감싸서 반환된다
# # 구분자를 특정하고 싶은 경우
# fruits = "딸기,거봉,키위,사쿠란보"
# print(fruits.split(",")) # ['딸기', '거봉', '키위', '사쿠란보']
#   # 문자열 콤마를 기준으로 분할

# # 원래는 공백이 영향을 받지만 print할때는 받지 않는다
# fruits2 = "딸기, 거봉, 키위, 사쿠란보"
# print(fruits2.split(",")) # ['딸기', ' 거봉', ' 키위', ' 사쿠란보']

# # 리스트의 인덱스
# fruits_list = fruits.split(",")
# print(fruits_list) # ['딸기', '거봉', '키위', '사쿠란보']

# # 거봉만 출력하기
# print(fruits_list[1]) # 거봉
# print(fruits_list[3]) # 사쿠란보
# print(fruits_list[-1]) # 사쿠란보

# # split 횟수 제한
# num = "010-1234-1234"
# # ["010", "1234-1234" ]
# print(num.split("-", 1))

# bam = "a,b,c,d"
# print(bam.split(","))

# # ==============================================================

# # join() - 리스트의 여러 조각을 하나의 문자열로 합치기
# # "구분자".join(리스트)

# # fruits_list.join(",")

# "-".join(fruits_list) # "딸기-거봉-키위-사쿠란보"
# ",".join(fruits_list) # "딸기,거봉,키위,사쿠란보"
# ", ".join(fruits_list) # "딸기, 거봉, 키위, 사쿠란보"

# ab = ["2025","01","15"]
# print("-".join(ab))


# # pyThon 출력하기

# word = "python"
# # 방법1 )srtip + capitalize
# # print(word[:2]) + word.strip("py").capitalize

# # 방법2 ) replace 사용
# print(word.replace("t","T"))

# # 방법3 ) 슬라이싱 + T만 upper 사용
# print(word[:2] + word[2].upper() + word[3:])

# # 방법4 ) 인덱싱으로 글자 하나씩 연결
# print(word[0] + word[1] + word[2] + word[3].upper() + word[4] + word[5])

# # 방법5 ) 인덱싱 + strip + title
# print(word[:2] + word.strip("py").title())

# # 방법6) split + join
# print(word.split("t")) # ["py", "hon"]
# print("T".join(word.split("t"))) # pyThon

# # =====================================================================

# # print 함수의 sep, end
# print("2026", "07", "27") # 2026 07 27
# print("2026", "07", "27", sep="사랑해") # 2026사랑해07사랑해27
# # 공백대신에 문자열 삽입되어 이어짐

# print("안녕", "하세") # 안녕 하세
# print("안녕", "하세", end="요\n") #안녕 하세요
# # end 속성 사용 시 출력문 마지막에 해당 문자열이 붙어 삽임

# # print 함수 + 사용 시 sep과 end
# print("안녕", "하세", end="요" + "이렇게?!")  #안녕 하세요안녕 하세요이렇게?

# # 기본적으로 print문에는 sep으로 공백 한 칸,
# # end로 |n(줄바꿈)이 적용되어 있음
# # 근데 개발자가 각 속석을 직접 부여할 경우
# # 기본값이 아닌 전달받은 속성값을 적용

# note = "2026/07/27"
# notebo = note.split("/")
# print("-".join(notebo))

# ttt = "1, NORMAL ,25.3"
# bbb = ttt.split(",") # ['1', ' NORMAL ', '25.3']
# ccc = bbb[1].strip().lower()
# print(ccc)

# # =================================================================

# # f-string - 문자열 안에 변수 값을 바로 끼워 넣는 출력
# # f"설비{code}점검"은"설비 EQP-001 점검"
# # f"{}" 형태로 변수를 중괄호로 감쌈
# # 따옴표 앞 f가 중괄호를 변수로 해석하라는 신호
#   # name = "홍길동"
#   # age = 25
#   # print(f"{name}님은 {age}살입니다")
#   # code = "EQP-001"
#   # print(f'설비 {code} 점검 완료')

# name = "PUMP_A"
# temp = 87

# print("설비" + name + " 온도 " + str(temp))

# # f-string
# print(f"설비 {name}, 온도 {temp}도")
# # 따옴표 밖에 f 작성하기
# # 변수명은 꼭 {중괄호}에 감싸기

# # f-string 연산
# hour = 8

# # 우리는 하루에 8시간 수업을 듣고, 이는 480분 입니다.

# print(f"우리는 하루에 {hour} 시간 수업을 듣고, 이는 {hour*60}분 입니다.")

# a = 57
# b = 73
# c = 104

# print(f"{(a + b +c) /3}")

# value = 87.456
# print(f"{value:.1f}")
# print(f"{value:.2f}")

word = "5, sensor_02, WARNING, 0.78912"

parts = word.strip().split(",")
sen = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())
print(f"[센서 {sen}] 상태 {status}, 측정값 {value:.2f}")
