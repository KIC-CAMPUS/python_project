from .jaccard import jaccard_similarity
from .boyer_moore_algorithm import boyer_moore
from .stopword import remove_stopwords_and_special_characters
from nltk import word_tokenize
import pandas as pd

# 표절률 구하는 함수
def boyer_moore_matching_sentences(tokens1, tokens2):
   match_count = 0
   if isinstance(tokens1, list):
      src_words = tokens1
   else:
      src_words = tokens1.split()

   if isinstance(tokens2, list):
      pat_words = tokens2
   else:
      pat_words = tokens2.split()

   pat_length = len(pat_words)
   match_word_count = boyer_moore(tokens1, tokens2)

   match_c = 0  # Initialize match_c outside the conditional blocks
   denom = 0    # Initialize denom outside the conditional blocks
   ratio = 0    # Initialize ratio outside the conditional blocks

   # 문장의 각 단어에 대해 Boyer-Moore 알고리즘 실행
   for i in range(0, len(src_words) - 1, 2):
      for j in range(len(pat_words)):
         match_count += boyer_moore(src_words[i] + src_words[i + 1], pat_words[j])

   if match_word_count < 1:
      match_c = match_count * 2
      denom = pat_length + len(src_words)
      ratio = match_c / denom

      return ratio

   else:
      return 1
   
# 여러 문장중에서 입력한 문장과 가장 가까운 유사도 구하기
def find_most_similar(sentence1, sentences):
   max_similarity = 0
   most_similar_sentence = ""

   for sentence in sentences:
      similarity = jaccard_similarity(sentence1, sentence)
      if similarity > max_similarity:
         max_similarity = similarity
         most_similar_sentence = sentence

   return most_similar_sentence, max_similarity

df = pd.read_csv(r"C:\Users\KITCOOP\Desktop\ResumeDatas.csv")
sentences = df["answer"].tolist()

# 입력 문장과 비교 대상 문장 간의 유사도 계산
def sentence_plagiarism_rate(sentence1, sentences=sentences):
   # 전체 문장의 유사도 합 초기화
   total_ratio = 0
   for n, query_sentence in enumerate(sentence1):
      most_similar, similarity_score = find_most_similar(query_sentence, sentences)
      print(f"For sentence {n + 1}, Input sentence: '{query_sentence}', Most similar sentence: '{most_similar}' Similarity Score: {similarity_score:.4f}")
      print("------")

      filtered_sentence1 = remove_stopwords_and_special_characters(most_similar)
      filtered_sentence2 = remove_stopwords_and_special_characters(query_sentence)

      tokens1 = word_tokenize(filtered_sentence1)
      tokens2 = word_tokenize(filtered_sentence2)

      # print(f"토큰화된 단어: {tokens1}")
      # print(f"토큰화된 단어: {tokens2}")

      pat_length = len(tokens2)
      tokens_length = len(tokens1)
      matchwordCount = boyer_moore(most_similar, query_sentence)

      result = boyer_moore_matching_sentences(tokens1, tokens2)

      total_ratio += result
      print("result", result)

   average_ratio = total_ratio / len(sentence1)
   rounded_average_ratio = round(average_ratio, 1)
   return rounded_average_ratio

# sentence1 = df["answer"][20000]
# sentence_plagiarism_rate = reulst_sentence([sentence1])