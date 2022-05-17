# 비계층적 군집분석 : k-means - 평균을 새로운 기준으로 갱신해가며 군집화

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
x, _ = make_blobs(n_samples = 150, n_features = 2, center = 3, cluster_std = 0.5, 
                  shuffle = True, random_state = 0)

print(x)

