# #기존 배열의 모든 요소에 3을 곱한 값을 가진 새 리스트 생성
# temps = [1, 5, 2, 7, 4, 8 ,10, 3]

# doubled = []

# for t in temps:
#   doubled.append(t * 3)
# print(doubled)

# # 조건에 맞는 값으로 새 리스트 만들기
# high = []
# low = []

# for t in temps:
#   if t < 5:
#     low.append(t)
#   else:
#     high.append(t)


# temps = [30, 34, 36, 28, 37]

# over = []
# for i in temps:
#     if i > 30:
#         over.append(i)
#         over.sort(reverse=True)

# print(over)
# print(len(over))

# temps = [30, 34, 36, 28, 37]

# sub = []
# for i in temps:
#     sub.append(i * 1.8 + 32)
# print(sub)


# 리스트 안의 리스트

# row = [["펌프", 25], ["모터", 32], ["압축기", 28]]

# # 표 (행,열)처럼 한 줄에 여러 값이 묶인 데이터
# # 바깥 대괄호를 "행", 안쪽 인덱스 리스트를 "열"

# print(row[0])

# # 중첩된 리스트 안의 값에 접근
# print(row[1][1])
# # 1. rows[1]을 찾음 -> ["모터", 32]
# # 2. print(["모터, 32"][1]) -> [1]앞의 리스트에서 1번 인덱스값에 접근
# # 중첩된 리스트 내부의 값은 대괄호를 여러번 이어서 접근한다

# # 리스트 안의 리스트 온도값만 출력하기
# for r in row:
#     print(r[0])


temps = [36, 38, 40, 42, 44, 46, 48, 50]

total = 0
for i in temps:
    total += i
print("전체 평균", total / len(temps))

hot = []
for i in temps:
    if i > 40:
        hot.append(i)

hot_total = 0
for h in hot:
    hot_total += h

print("고온갯수", len(hot))
print("고온 평균", hot_total / len(hot))
