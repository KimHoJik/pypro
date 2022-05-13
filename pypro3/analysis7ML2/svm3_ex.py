from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

heartdata = pd.read_csv('../testdata/Heart.csv')
print(heartdata.info())
data = heartdata.drop(['Thal', 'ChestPain'], axis = 1)
data.loc[data.AHD=='Yes', 'AHD'] = 1
data.loc[data.AHD=='No', 'AHD'] = 0

print(heartdata.isnull().sum())  # Ca에 4개
Heart = data.fillna(data.mean())  # 
label = Heart['AHD']
features = Heart.drop(['AHD'], axis = 1)

data_train, data_test, label_train, label_test = \
    train_test_split(features, label, test_size = 0.3, random_state = 12)
    
model = svm.LinearSVC(C =10).fit(data_train, label_train)

# 예측치 구하기
pred = model.predict(data_test)
print('예측값 : ', pred[:10])
print('실제값 : ', np.array(label_test)[:10])

print(model.score(data_train, label_train))
print(model.score(data_test, label_test))
print('분류 정확도 : ', metrics.accuracy_score(label_test, pred))