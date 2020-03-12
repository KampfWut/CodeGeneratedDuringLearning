# Author:   Jin Xu
# Data:     2019-02-13
# Function: Implementation of logistic regression

#--------------------------     import package    --------------------------#

import matplotlib.pyplot as plt
from C_LogisticRegression import *  
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
 
#---------------------------     main process     ---------------------------#

iris = load_iris()
data = iris.data
target = iris.target
X = data[0:100,[0,2]]
y = target[0:100]
print(">> X:\n{}".format(X[0:10]))
print(">> Y:\n{}".format(y[0:10]))

y = y.reshape((-1,1))
print(">> Change Y to:\n{}".format(y[0:10]))
# add the x0=1
one = np.ones((X.shape[0],1))
X_train = np.hstack((one,X))
print(">> Change X to:\n{}".format(X_train[0:10]))

print("\n>> Start Logistic regression:")
classify = logistic()
loss = classify.train(X_train, y, learn_rate = 0.01, num_iters = 8000)
print("\n>> Logistic regression Answer:")
print("   theta0: {}, theta1: {}, theta2: {}".format(classify.W[0,0], classify.W[1,0], classify.W[2,0]))

plt.figure(1)
plt.plot(loss)
plt.xlabel('Iteration number')
plt.ylabel('Loss value')
  
plt.figure(2)
label = np.array(y)
index_0 = np.where(label == 0)
plt.scatter(X[index_0, 0], X[index_0, 1], marker='x', color = 'b', label = '0', s = 15)
index_1 =np.where(label == 1)
plt.scatter(X[index_1,0], X[index_1,1], marker='o', color = 'r', label = '1', s = 15)
 
#show the decision boundary
x1 = np.arange(4, 7.5, 0.5)
x2 = (- classify.W[0] - classify.W[1] * x1 ) / classify.W[2]
plt.plot(x1, x2, color = 'y')
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend(loc = 'upper left')

plt.show()