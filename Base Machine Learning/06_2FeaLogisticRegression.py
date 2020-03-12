# 06. 2特征逻辑回归
# 徐进 2019.02.03

import math
import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt
import sympy as smp

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Step1. 生成数据
print("\n   >>> Step 1 <<<   \n")
x, y, z = [], [], []
m = 30
for i in range(30):
    tempx, tempy = rd.randint(0,10), rd.randint(0,10)
    if tempx + tempy >= 10:
        z.append(1)
    else:
        z.append(0)
    x.append(tempx)
    y.append(tempy)

# Output
print(">> Data: ")
print("   x:        {}".format(x))
print("   y:        {}".format(y))
print("   z:        {}".format(z))

# Step.2 数据处理
print("\n   >>> Step 2 <<<   \n")
X = []
for i in range(0, m):
    temp = [1]
    temp.append(x[i])
    temp.append(y[i])
    X.append(temp)
X = np.array(X)
Y = np.array(z).reshape((-1,1))

# Output
print(">> Change Data: ")
print("   X:\n{}".format(X[0:5]))
print("   Y:\n{}".format(Y[0:5]))

# Step.3 逻辑回归
print("\n   >>> Step 3 <<<   \n")
from C_LogisticRegression import *  
print("\n>> Start Logistic regression:")
classify = logistic()
loss = classify.train(X, Y, learn_rate = 0.01, lam = 0, num_iters = 12000)
print("\n>> Logistic regression Answer:")
print("   theta0: {}, theta1: {}, theta2: {}".format(classify.W[0,0], classify.W[1,0], classify.W[2,0]))

# Output
plt.figure(1)
plt.title("Error Plot")
plt.plot(loss)
plt.xlabel('Iteration number')
plt.ylabel('Loss value')
  
plt.figure(2)
plt.title("Data Plot")
for i in range(0, m):
    if z[i] == 1:
        plt.plot(x[i], y[i], "rx")
    else:
        plt.plot(x[i], y[i], "bo")
x1 = np.arange(0, 10, 0.5)
x2 = (- classify.W[0] - classify.W[1] * x1 ) / classify.W[2]
plt.plot(x1, x2, color = 'y')
plt.xlabel('X1')
plt.ylabel('X2')

plt.show()



'''
# Step2. 逻辑回归
print("\n   >>> Step 2 <<<   \n")

alpha = 0.000003
theta0, theta1, theta2 = 1, 1, 1
count = 0
nowJ = 0
for i in range(0, m):
    h = 1.0 / ( 1 + math.e ** (-(theta0 + theta1 * x[i] + theta2 * y[i])) )
    nowJ = nowJ + z[i] * math.log(h) + (1-z[i]) * math.log(1-h)
nowJ = nowJ / m * (-1)
subvalue = 9999999999999999999
errorList = []

# MainBody
print(">> Logistic Regression Start")
while count <= 1000000 and subvalue > 0:
    count = count + 1
    lastJ = nowJ

    h = 1.0 / ( 1 + math.e ** (-(theta0 + theta1 * x[i] + theta2 * y[i])) )
    tempt0 = 0
    for i in range(0, m):
        tempt0 = tempt0 + (h - z[i]) * 1
    tempt0 = tempt0 / m
    tempt1 = 0
    for i in range(0, m):
        tempt1 = tempt1 + (h - z[i]) * x[i]
    tempt1 = tempt1 / m
    tempt2 = 0
    for i in range(0, m):
        tempt2 = tempt2 + (h - z[i]) * y[i]
    tempt2 = tempt2 / m
    theta0 = theta0 - alpha * tempt0
    theta1 = theta1 - alpha * tempt1
    theta2 = theta2 - alpha * tempt2
    
    nowJ = 0
    for i in range(0, m):
        h = 1.0 / ( 1 + math.e ** (-(theta0 + theta1 * x[i] + theta2 * y[i])) )
        nowJ = nowJ + z[i] * math.log(h) + (1-z[i]) * math.log(1-h)
    nowJ = nowJ / m * (-1)

    subvalue = lastJ - nowJ
    errorList.append(nowJ)
    print("  Count {:5d}: NowJ is {:.8f}, Subvalue is {:.8f}".format(count, nowJ, subvalue))

# Output
print("\n>> Ans:")
print("   theta0: {}, theta1: {}, theta2: {}".format(theta0, theta1, theta2))
print("   Function: y = 1 / ( 1 + e^(-{} - {}x - {}y))".format(theta0, theta1, theta2))

stepx = np.array(np.arange(0, 20, 1))
stepy = np.array(np.arange(0, 20, 1))
ans = 1 / ( 1 + math.e ** ((-1) * theta0 - theta1 * stepx - theta2 * stepy))

# theta0 + theta1 * x + theta2 * y = 0 -> -theta0 - theta2 * y = theta1 * x
dbstep = np.array(np.arange(0, 10, 0.1))
dbvalue = (-theta0 - theta2 * dbstep)/theta1
print("   Decision boundary: {}x + {}y + {} = 0".format(theta1, theta2, theta0))

plt.plot(list(dbvalue), list(dbstep), "y-", label = "decision boundary")
plt.legend(loc='best')
plt.savefig("06_Fig1_DataPlot2D.pdf")

fig = plt.figure(2)
ax = fig.gca(projection='3d')
plt.title("Data Plot 3D")
ax.scatter(x, y, z, "bo")
ax.plot(stepx, stepy, ans, "y-")
plt.savefig("06_Fig1_DataPlot3D.pdf")

plt.figure(3)
plt.title("Error Plot")
plt.plot(errorList, "b-")
plt.savefig("06_Fig2_ErrorPlot.pdf")

plt.show()
'''