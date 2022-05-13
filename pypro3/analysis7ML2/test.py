# [XGBoost 문제] 
# kaggle.com이 제공하는 'glass datasets'
# 유리 식별 데이터베이스로 여러 가지 특징들에 의해 7가지의 label(Type)로 분리된다.
#
# RI    Na    Mg    Al    Si    K    Ca    Ba    Fe    
#  Type
# glass.csv 파일을 읽어 분류 작업을 수행하시오.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from xgboost import plot_importance
from lightgbm import LGBMClassifier

dataset = pd.read_csv("../testdata/glass.csv")
print(dataset.head(3))
x_feature = dataset.data
y_label = dataset.target
print(dataset.feature_names)

glass_df = pd.DataFrame(data = x_feature, columns=dataset.feature_names)
pd.set_option('max_columns', None)
print(glass_df.head(3), glass_df.shape)
print(dataset.target_names)
print(np.sum(y_label == 0))
print(np.sum(y_label == 1))

x_train, x_test, y_train, y_test = train_test_split(x_feature, y_label, test_size = 0.3, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model = xgb.XGBClassifier(booster='gbtree', max_depth = 6, n_estimators = 500).fit(x_train, y_train)

print(model)
pred = model.predict(x_test)
print('예측값 : ', pred[:10])
print('실제값 : ', y_test[:10])
from sklearn import metrics
print('분류 정확도 :', metrics.accuracy_score(y_test, pred))
print('분류 보고서 :', metrics.classification_report(y_test, pred))



