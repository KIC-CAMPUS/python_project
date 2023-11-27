def boyer_moore(src, pat):
   pattern = list(pat)
   string = list(src)
   bad_match_table = {}

   # 나쁜 매치 테이블 초기화
   for i in range(len(pat)):
      bad_match_table[pattern[i]] = len(pat) - i - 1

   bad_match_table[pattern[len(pat) - 1]] = len(pat)
   bad_match_table['*'] = len(pat)

   i = len(pat) - 1
   counter_for_time = 0

   while i < len(src):
      temp_i = i
      for j in range(len(pat) - 1, -1, -1):
         if pattern[j] == string[i]:
               i -= 1

               if j == 0:
                  # 패턴이 발견되면 1 반환
                  return 1
         else:
               if string[temp_i] in bad_match_table:
                  # 나쁜 매치 테이블을 사용하여 이동
                  i = i + bad_match_table[string[temp_i]]
                  break
               else:
                  # '*'에 해당하는 값만큼 이동
                  i = i + len(pat)
                  break

         # 반복문 실행 횟수 측정
         counter_for_time += 1
   # 패턴이 발견되지 않으면 0 반환
   return 0