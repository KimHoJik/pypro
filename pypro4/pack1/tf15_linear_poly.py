# 지역별 인구증가율과 고령인구비율(통계청 시각화 자료에서 발췌) 데이터로 선형회귀분석 및 시각화
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

population_inc = [0.3, -0.78, 1.26, 0.03, 1.11, 15.17, 0.24, -0.24, -0.47, -0.77, -0.37, -0.85, -0.41, -0.27, 0.02, -0.76, 2.66]
print(len(population_inc))
population_old = [12.27, 14.44, 11.87, 18.75, 17.52, 9.29, 16.37, 19.78, 19.51, 12.65, 14.74, 10.72, 21.94, 12.83, 15.51, 17.14, 14.42]

plt.plot(population_inc,population_old,'bo')
plt.xlabel('지역별 인구증가율 (%)')
plt.ylabel('고령인구비율 (%)')
plt.show()

# 지역별 인구증가율과 고령인구비율 : 이상(극단)치 제거 - 세종시 데이터
population_inc = population_inc[:5] + population_inc[6:]  # 5번째는 제외
population_old = population_old[:5] + population_old[6:]
print(len(population_inc))

plt.plot(population_inc,population_old,'bo')
plt.xlabel('지역별 인구증가율 (%)')
plt.ylabel('고령인구비율 (%)')
plt.show()