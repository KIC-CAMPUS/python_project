# 자카트 유사도
def jaccard_similarity(sentence1, sentence2):
   set1 = set(sentence1.split())

   # Ensure that sentence2 is a string
   if isinstance(sentence2, float):
      sentence2 = str(sentence2)

   set2 = set(sentence2.split())
   intersection = len(set1.intersection(set2))
   union = len(set1) + len(set2) - intersection
   return intersection / union