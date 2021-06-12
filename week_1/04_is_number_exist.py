input = [4, 5, 6, 1, 2, 3]  # 입력값에 따라서 성능이 변화할 수 있다


def is_number_exist(number, array):
                            # 시간 복잡도
    for element in array:  # array 길이만큼 아래 연산 실행
        if number == element:  # 비교 연산 1회 실행
            return True  # N * 1 = N 만큼

    return False


result = is_number_exist(3, input)
print(result)
