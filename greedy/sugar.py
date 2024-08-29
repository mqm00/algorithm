sugar = int(input())  # 설탕의 무게를 입력받습니다.
count = 0  # 봉지의 개수를 세는 변수입니다.

# 가능한 최대 5kg 봉지를 사용하면서 남은 설탕이 3kg 봉지로 나누어 떨어지는지 확인합니다.
while sugar >= 0:
    if sugar % 5 == 0:  # 설탕이 5로 나누어 떨어지면
        count += sugar // 5  # 5kg 봉지의 개수를 추가합니다.
        print(count)
        break
    sugar -= 3  # 5로 나누어 떨어지지 않으면 3kg 봉지를 하나 사용합니다.
    count += 1  # 봉지의 개수를 하나 추가합니다.
else:
    print(-1)  # 설탕을 정확히 나눌 수 없는 경우 -1을 출력합니다.
