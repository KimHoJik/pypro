# XGBoost는 Gradient Boosting 알고리즘을 분산 환경에서도 실행할 수 있도록 구현해 놓은 라이브러로 
# Regression, Classification 문제를 모두 지원하며, 성능과 자원 효율이 좋아서 인기 있는 알고리즘이다.
# RandomForest와 마찬가지로 XGBoost는 여러 개의 Decision Tree를 조합해서 사용하는 Ensemble 알고리즘이다
# pip install xgboost
# pip install lightgbm

# breast_cancer dataset 사용
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from xgboost import plot_importance
from lightgbm import LGBMClassifier
import xgboost as xgb
import matplotlib.pyplot as plt

dataset = load_breast_cancer()
x_feature = dataset.data
y_label = dataset.target
# print(dataset.feature_names)

cancer_df = pd.DataFrame(data = x_feature, columns = dataset.feature_names)
pd.set_option('max_columns', None)
print(cancer_df.head(2), cancer_df.shape)  # (569, 30)
print(dataset.target_names)  # ['malignant' 'benign']
print(np.sum(y_label == 0))  # malignant : 212
print(np.sum(y_label == 1))  # benign : 357

x_train, x_test, y_train, y_test = train_test_split(x_feature, y_label, test_size = 0.2, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  # (455, 30) (114, 30) (455,) (114,)

model = xgb.XGBClassifier(booster='gbtree', max_depth = 6, n_estimators = 500).fit(x_train, y_train)
# model = xgb.LGBMClassifier(booster='gbtree', max_depth = 6, n_estimators = 500).fit(x_train, y_train)

print(model)
pred = model.predict(x_test)
print('예측값 : ', pred[:10])
print('시제값 : ', y_test[:10])

from sklearn import metrics
print('분류 정확도 : ', metrics.accuracy_score(y_test, pred))
print('분류 보고서 : ', metrics.classification_report(y_test, pred))

# 시각화
fig, ax = plt.subplots(figsize = (10, 12))
plot_importance(model, ax = ax)
plt.show()