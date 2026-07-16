# 여러줄 문자열

# notice = """설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검"""

# print(notice)


# notice = "설비 점검 안내 \n1. 전원 확인\n2. 센서 점검"
# print(notice)

# tap = "이름/상태"
# print(tap) #이름\상태 > 첫 번째 \는 이스케이프 문자라는 것을 알리는 용도

# set = "PUMP_A"
# status = "정상"
# oper = 1200
# view = "2026-07-16"

# set_up = (
#     "설비: " + set + "\n상태: " + status + "\n가동: " + str(oper) + "\n점검: " + view
# )

# print(set_up)

# # ==================================================
# word = "PHYTON"
# print(word[0], word[5], word[3])

# abc = "abcdefghijklnmopqrstuvwxyz"
# # print(
# #     abc[7]
# #     + abc[0]
# #     + abc[12]
# #     + abc[7]
# #     + abc[-2]
# #     + abc[4]
# #     + abc[14]
# #     + abc[12]
# #     + abc[6]
# #     + abc[7]
# #     + abc[4]
# #     + abc[4]


# print(abc[::-3])


# start = "temp_sensor"
# print(start[5:])


# word = "sensor_01"
# print(word[-2:])


# word = "PHTYON"
# print(word[::-1])

# =============================================
# 문자열의 길이 반환
# print(len("hello world"))
# print(len(" "))

# var = "여러분 한시간 만 더 하면 됩니다 조금만 힘내세요!"
# print(len(var))

# num = "01012345678"
# print(len(num))

# text = "a,b,c,d"
# print(text.count(","))

# print("hong@company.com".find("@"))

email = "hong@company.com"
at = email.find("@")
user_id = email[:at]
print(user_id)
