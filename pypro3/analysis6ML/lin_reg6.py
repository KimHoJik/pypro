# Advertising.csv : 여러 매체를 통한 광고비 판매량 추정치 얻기

import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

advdf = pd.read_csv("../testdata/Advertising.csv", usecols=[1,2,3,4])
print(advdf.head(3), advdf.shape)  # (200, 4)

print('상관계수(r) : ', advdf.loc[:, ['sales', 'tv']].corr())  # 0.782224
print('상관계수(r) : ', advdf.loc[:, ['sales', 'newspaper']].corr())  # 0.228299
print('상관계수(r) : ', advdf.loc[:, ['sales', 'radio']].corr())  # 0.576223

print()
# 단순 선형회귀
lm = smf.ols(formula = 'sales ~ tv', data = advdf).fit()
print(lm.summary())
print('설명력 : ', lm.rsquared)
print('p값 : ', lm.pvalues[1])

# 시각화
"""
plt.scatter(advdf.tv, advdf.sales)
plt.xlabel('tv')
plt.ylabel('sales')
x = pd.DataFrame({'tv':[advdf.tv.min(),advdf.tv.max()]})   추세선 긋기
y_pred = lm.predict(x)
plt.plot(x, y_pred, c='red')
plt.show()
"""
# 미지의 tv 광고비에 따른 상품 판매량 추정 
x_new = pd.DataFrame({'tv':[220.12, 55.66, 10]})
pred_new = lm.predict(x_new)
print('상품 판매량 추정치 : ', pred_new.values)

print('------')
print(advdf.corr())     # sales 와의 상관관계 : tv > radio > newspaper
lm_mul = smf.ols(formula = 'sales ~ tv + radio + newspaper', data = advdf).fit()
print(lm_mul.summary()) # Adj. R-squared: 0.896, p-value:1.58e-96 < 0.05 유의한 모델

lm_mul = smf.ols(formula = 'sales ~ tv + radio', data = advdf).fit()
print(lm_mul.summary()) # Adj. R-squared: 0.896, p-value:1.58e-96 < 0.05 유의한 모델
# newspapers는 모델의 성능에 영향을 주지 못하는변수

