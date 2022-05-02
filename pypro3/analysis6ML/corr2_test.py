# 상관관계 문제)
# https://github.com/pykwon/python 에 있는 Advertising.csv 파일을 읽어 tv,radio,newspaper 간의 상관관계를 파악하시오. 
# 그리고 이들의 관계를 heatmap 그래프로 표현하시오. 

import json 
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family='malgun gothic')

data = pd.read_csv("../testdata/Advertising.csv")
print(data)
df = pd.DataFrame(data, columns = ('no', 'tv', 'radio', 'newspaper'))
df = df.set_index('no')
print(df)

print(df.corr())
print(df.corr(method='pearson'))

# heatmap
import seaborn as sns
sns.heatmap(df.corr())
plt.show()