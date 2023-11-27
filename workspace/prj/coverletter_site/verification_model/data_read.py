import pandas as pd
import os

com_path = r'%s' % os.getcwd() + '/coverletter_site/verification_model/data/com_f.csv' # 입사 포부
for_path = r'%s' % os.getcwd() + '/coverletter_site/verification_model/data/for_f.csv' # 지원 동기
growth_path = r'%s' % os.getcwd() + '/coverletter_site/verification_model/data/growth_f.csv' # 성격
teamwork_path = r'%s' % os.getcwd() + '/coverletter_site/verification_model/data/teamwork_f.csv' # 팀워크
etc_path = r'%s' % os.getcwd() + '/coverletter_site/verification_model/data/etc_f.csv' # 기타

path_data_sentences = {
   1 : pd.read_csv(com_path)["Sentence"].tolist(),
   2 : pd.read_csv(for_path)["Sentence"].tolist(),
   3 : pd.read_csv(growth_path)["Sentence"].tolist(),
   4 : pd.read_csv(teamwork_path)["Sentence"].tolist(),
   5 : pd.read_csv(etc_path)["Sentence"].tolist(),
}