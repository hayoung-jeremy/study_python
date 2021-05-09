# for

days = ["월", "화", "수", "목", "금"]

for day in days:
    if day is "수":
        # break를 설정한 직전 데이터까지만 출력됨
        break # 월 화
    else:
        print(day)