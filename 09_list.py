# # list는 python의 자료형 중 하나
# # 여러 개의 값을 [대괄호]에 감싸서 순서대로 저장
# # 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가지게 됨

# # temps = [35, 36, 37, 38]
# # float_temp = [36.4, 36.5, 36.6, 36.7]
# # machines = ["펌프", 압축기", "모니터"]

# # # 자료형이 달라도 한 리스트에 담을 수 있음
# # mixed = ["펌프", 78, True]

# # print(temp[2])

# # print(len(temps)

# # # 리스트에 담긴 값의 갯수 변수에 저장
# # temps_lenght = len(temps)

# # temps = [30, 35, 34, 33, 32, 38]
# # print(temps[0])
# # print(temps[2])
# # print(temps[-1])

# # first = temps[0]
# # last = temps[-1]

# # print(first + last)
# # print((first + last) / 2)

# # # print(f"temps: {}")

# # temps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(temps[:3])
# # print(temps[-3:])
# # print(len(temps[:3]))


# han = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# # first = han[:6]
# # second = han[-6:]
# # print(len(first))
# # print(len(second))

# # # 인덱스로 특정 값 바꾸기
# # print("원본", han)
# # han[5] = 958
# # print("5번 인덱스 값 변경 결과:", han)

# # # in (존재확인)
# # machines = ["펌프", "압축기", "모터"]
# # print("펌프" in machines)

# temps = [60, 54, 71, 83, 90]
# print(71 in temps)

# f = temps.index(71)
# temps[f] = 52
# print(temps)
# print(71 in temps)

# empty = []
# empty.append(36)
# empty.insert(0,48)
# empty.extend([11,51])

# temps = [10, 11, 12, 13, 14]


# print(temps.pop(3))
# print(temps)
# print(temps.pop(3))

# temps = [25, 26, 24, 28, 27]
# del temps[1:3]  # 구간 삭제도 가능
# print(temps)

# temps = [1, 2, 3, 4, 999, 5]
# temps.remove(999)
# print(temps)

# x = temps.pop(2)
# print(x)

# del temps[0]
# print(temps)

# 리스트 정렬하기
# 리스트.sort()
# 데이터를 정렬하는 친구
# 기본적으로 오름차순(작은 숫자부터 큰 숫자까지)
# 내림차순으로 정렬하고 싶은 경우에는 .sort(reverse=True)

# n = [37, 2, 8, 109, 1004, -1, 22]
# n.sort()
# print(n)

# n.sort(reverse=True)
# print(n)

# f = ["텀블러", "일회용컵", "텀블러", "일회용컵"]
# print(f.count("일회용컵"))

temps = [22, 24, 24, 26, 27, 28, 30]
temps.sort()
print(temps)
temps.sort(reverse=True)
print(temps)
print(temps.count(24))
print(temps.index(24))
