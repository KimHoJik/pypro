# 선형회귀 : mtcars dataset
import statsmodels.api
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars)
print(mtcars.columns)
print(mtcars.describe())

print(mtcars.corr())
# print(mtcars.corrcoef(mtcars.hp, mtcars.mpg))
# print(mtcars.corrcoef(mtcars.wt, mtcars.mpg))

"""
# 시각화
plt.scatter(mtcars.hp, mtcars.mpg)
plt.xlabel('마력수')
plt.ylabel('연비')
slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1)
plt.plot(mtcars.hp, mtcars.hp * slope + intercept, 'r')
plt.show()
"""

# 단순 선형회귀
result = smf.ols('mpg ~ hp', data = mtcars).fit()
print(result.summary())
print(result.summary().tables[1])

print('마력 수 110에 대한 연비 예측 : ', -0.0682 * 110 + 30.0989)
print('마력 수 50에 대한 연비 예측 : ', -0.0682 * 50 + 30.0989)

print('------')
# 다중 선형회귀
result2 = smf.ols('mpg ~ hp + wt', data = mtcars).fit()
print(result2.summary())

print('마력수 110 + 차체 무게 5 에 대한 연비 예측 : ', (-0.0318 * 110) + (-3.8778 * 5) + 37.2273)

print('---\n추정치 구하기 :  predict---')
result3 = smf.ols('mpg ~ wt', data = mtcars).fit()
print('결정계수 : ', result3.rsquared)  # 0.7528
print('p-value : ', result3.pvalues[1])  # 1.2939587013504974e-10 < 0.05
pred = result.predict()  # 학습 데이터로 예측
print(pred)

print(mtcars.mpg[0])
print(pred[0])

# DataFrame에 실제값과 예측값 기억
data = {
    'mpg':mtcars.mpg,
    'mpg_pred':pred
}

df = pd.DataFrame(data)
print(df)

# 새로운 차체 무게로 연비예측
# 차체 무게 여러개
new_wt = pd.DataFrame({'wt':[6, 3, 1]})
new_pred2 = result3.predict(new_wt)
print('예상 연비 : \n', new_pred2)

# 새로운 차체 무게로 연비 예측
mtcars.wt = float(input('차체무게 : '))
new_pred = result3.predict(pd.DataFrame(mtcars.wt))
print('차체 무게:{}일 때 예상 연비는 {}'.format(mtcars.wt[0], new_pred[0]))