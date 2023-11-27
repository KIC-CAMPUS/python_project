import re
from konlpy.tag import Okt

# 불용어 제거
def remove_stopwords_and_special_characters(sentence):
   okt = Okt()
   # KoNLPy 형태소 분석을 통한 명사 추출
   nouns = okt.nouns(sentence)
   # 특수문자를 제외한 명사들을 저장
   words = [word for word in nouns if re.match("^[가-힣0-9a-zA-Z]+$", word)]
   return ' '.join(words)