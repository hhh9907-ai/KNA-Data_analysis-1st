# 여러줄 문자열

# notice = """설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검"""

# print(notice)


# notice = "설비 점검 안내 \n1. 전원 확인\n2. 센서 점검"
# print(notice)

# tap = "이름/상태"
# print(tap) #이름\상태 > 첫 번째 \는 이스케이프 문자라는 것을 알리는 용도

set = "PUMP_A"
status = "정상"
oper = 1200
view = "2026-07-16"

set_up = (
    "설비: " + set + "\n상태: " + status + "\n가동: " + str(oper) + "\n점검: " + view
)

print(set_up)
