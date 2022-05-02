# 모델 맛보기 4 : linregress를 사용. model 생성 O

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IQ에 따른 시험성적 값 예측
score_iq = pd.read_csv("../testdata/score_iq.csv")
print(score_iq.info())
print(score_iq.head(3), score_iq.shape)  # (150, 6)

x = score_iq.iq
y = score_iq.score

# 상관계수 확인
print(np.corrcoef(x, y)[0, 1])  # numpy
print(score_iq.corr())  # pandas

# plt.scatter(x, y)
# plt.show()

# 선형회귀분석
model = stats.linregress(x, y)
print(model)
print('x slope : ', model.slope)
print('y intercept : ', model.intercept)
print('p value : ', model.pvalue)
# x slope :  0.6514309527270081
# y intercept :  -2.856447122197551
# p value :  2.8476895206672287e-50 < 0.05 유의한 모델
# y = model.slope * x + model.intercept
print('IP에 따른 점수 예측 : ', model.slope * 140 + model.intercept)  # 88.34388625958358
print('IP에 따른 점수 예측 : ', model.slope * 120 + model.intercept)  # 75.31526720504343
# linregress는 predict을 지원하지 않음
# 그래서 numpy의 polyval([slope, bias], x)을 이용
print('IP에 따른 점수 예측 : ', np.polyval([model.slope, model.intercept], 140)) 
print()
newdf = pd.DataFrame({'iq':[55, 66, 77, 88, 150]})
print('새로운 점수 예측 : ', np.polyval([model.slope, model.intercept], newdf).flatten())