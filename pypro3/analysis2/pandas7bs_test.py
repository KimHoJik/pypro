# pandas 문제 3)  타이타닉 승객 데이터를 사용하여 아래의 물음에 답하시오.
# 데이터 : http://cafe.daum.net/flowlife/RUrO/103
# https://github.com/pykwon/python/blob/master/testdata_utf8/titanic_data.csv
# titanic_data.csv 파일을 다운로드 후
# df = pd.read_csv('파일명',  header=None,,,)  
# 1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.
# cut() 함수 사용
# bins = [1, 20, 35, 60, 150]
# labels = ["소년", "청년", "장년", "노년"]
# 2) 성별 및 선실에 대한 자료를 이용해서 생존여부(Survived)에 대한 생존율을 피봇테이블 형태로 작성한다. 
# df.pivot_table()
# index에는 성별(Sex)를 사용하고, column에는 선실(Pclass) 인덱스를 사용한다.
# 출력 결과 샘플1 :       
# pclass    1    2    3
# sex            
# female    0.968085    0.921053    0.500000
# male    0.368852    0.157407    0.135447
# index에는 성별(Sex) 및 나이(Age)를 사용하고, column에는 선실(Pclass) 인덱스를 사용한다.
# 출력 결과 샘플2 : 위 결과물에 Age를 추가. 백분율로 표시. 소수 둘째자리까지.    예: 92.86
import pandas as pd
import numpy as np
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv', header=None)
print(df)
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
result_cut = pd.cut(labels, bins)
print(result_cut)
print(pd.value_counts(result_cut))
