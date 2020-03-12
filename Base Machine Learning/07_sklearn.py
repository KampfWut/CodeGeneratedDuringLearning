# 07. 使用sklearn
# 徐进 2019.02.04

import numpy as np
import matplotlib.pyplot as plt

# Step.1 生成数据
import sklearn.datasets

np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.20)

print(">>> data")
print("X:\n{}".format(X[0:10]))
print("Y:\n{}".format(y[0:10]))

plt.figure(1)
plt.scatter(X[:,0], X[:,1], s = 40, c = y, cmap = plt.cm.Spectral)

# Step.2 逻辑回归
from sklearn.linear_model import LogisticRegressionCV

clf = sklearn.linear_model.LogisticRegressionCV()
clf.fit(X, y)

def plot_decision_boundary(pred_func):
 
    # 设定最大最小值，附加一点点边缘填充
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
 
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
 
    # 用预测函数预测一下
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
 
    # 然后画出图
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)

plot_decision_boundary(lambda x: clf.predict(x))
plt.title("Logistic Regression")

plt.show()