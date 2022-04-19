# pandas 문제 1)
# a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 
# np.random.randn(9, 4)
# b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오
# c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용
from pandas import Series, DataFrame
import numpy as np
np.random.seed(1)
df1 = DataFrame(np.random.randn(9, 4))  #a
print(df1)
df1.columns = ['No1', 'No2', 'No3', 'No4']  #b
print(df1)
print(df1.mean(axis = 0))  # 평균, c

# pandas 문제 2) a : 10, b : 20, c : 30, d : 40
# a) DataFrame으로 위와 같은 자료를 만드시오. colume(열) name은 numbers, row(행) name은 a~d이고 값은 10~40.
# b) c row의 값을 가져오시오.
# c) a, d row들의 값을 가져오시오.
# d) numbers의 합을 구하시오.
# e) numbers의 값들을 각각 제곱하시오. 아래 결과가 나와야 함.
# f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5    아래 결과가 나와야 함.
# g) names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오. Series 클래스 사용.
data = [10, 20, 30, 40]
df2 = DataFrame(data, index = ['a', 'b', 'c', 'd'], columns = ['numbers']) #a
print(df2)
print(df2.loc['c'])  #b
print(df2.loc['a'], df2.loc['d'])  #c 
print(df2.sum(axis =0))  #d
print(df2.loc[:] ** 2)  #e
df2['floats'] = [1.5, 2.5, 3.5, 4.5]  # f
print(df2)
df2['names'] = Series(['길동', '오정', '팔계', '오공'], index = ['d', 'a', 'b', 'c'])  #g
print(df2)
