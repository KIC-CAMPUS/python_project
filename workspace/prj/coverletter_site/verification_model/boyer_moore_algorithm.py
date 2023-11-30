def boyer_moore(src, pat):
    pattern_list = list(pat)
    string_list = list(src)
    bad_match_table = {}

    # print("pattern_list:", pattern_list)
    # print("string_list:", string_list)

    # 패턴이 비어있는 경우 처리
    if not pattern_list or not string_list:
        return 0

    # 나쁜 매치 테이블 초기화
    for i in range(len(pat)):
        bad_match_table[pattern_list[i]] = len(pat) - i - 1

    bad_match_table[pattern_list[-1]] = len(pat)
    bad_match_table['*'] = len(pat)

    i = len(pat) - 1
    counter_for_time = 0

    while i < len(src):
        current_index = i
        for j in range(len(pat) - 1, -1, -1):
            if pattern_list[j] == string_list[i]:
                i -= 1

                if j == 0:
                    # 패턴이 발견되면 1 반환
                    return 1
            else:
                if string_list[current_index] in bad_match_table:
                    # 나쁜 매치 테이블을 사용하여 이동
                    i = i + bad_match_table[string_list[current_index]]
                    break
                else:
                    # '*'에 해당하는 값만큼 이동
                    i = i + len(pat)
                    break

        # 반복문 실행 횟수 측정
        counter_for_time += 1

    # 패턴이 발견되지 않으면 0 반환
    return 0
