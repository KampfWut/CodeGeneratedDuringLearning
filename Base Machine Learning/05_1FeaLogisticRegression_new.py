# 05. 基础单特征逻辑回归
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
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15]
y = [0, 0, 0, 1, 0, 0, 1, 1, 0,  1,  1,  1,  1]
m = len(x)

# Output
print(">> Data: ")
print("   x:        {}".format(x))
print("   y:        {}".format(y))
plt.figure(1)
plt.title("Data Plot")
for i in range(0, m):
    if y[i] == 0:
        plt.plot(x[i], y[i], "bo")
    else:
        plt.plot(x[i], y[i], "rx")

# Step2. 逻辑回归
print("\n   >>> Step 2 <<<   \n")

alpha = 0.001
theta0, theta1 = 1, 1
count = 0
nowJ = 0
for i in range(0, m):
    h = 1.0 / ( 1 + math.e ** (-(theta0 + theta1 * x[i] )) )
    nowJ = nowJ + y[i] * math.log(h) + (1-y[i]) * math.log(1-h)
nowJ = nowJ / m * (-1)
subvalue = 9999999999999999999
errorList = []

# MainBody
print(">> Logistic Regression Start")
while count <= 12000:
    count = count + 1
    lastJ = nowJ

    h = 1.0 / ( 1 + math.e ** (-(theta0 + theta1 * x[i] )) )
    tempt0 = 0
    for i in range(0, m):
        tempt0 = tempt0 + (h - y[i]) * 1
    tempt0 = tempt0 / m
    tempt1 = 0
    for i in range(0, m):
        tempt1 = tempt1 + (h - y[i]) * x[i]
    tempt1 = tempt1 / m
    theta0 = theta0 - alpha * tempt0
    theta1 = theta1 - alpha * tempt1
    
    nowJ = 0
    for i in range(0, m):
        h = 1.0 / ( 1 + math.e ** (-(theta0 + theta1 * x[i] )) )
        nowJ = nowJ + y[i] * math.log(h) + (1-y[i]) * math.log(1-h)
    nowJ = nowJ / m * (-1)

    subvalue = lastJ - nowJ
    errorList.append(nowJ)
    print("  Count {:5d}: NowJ is {:.8f}, Subvalue is {:.8f}".format(count, nowJ, subvalue))

# Output
print("\n>> Ans:")
print("   theta0: {}, theta1: {}".format(theta0, theta1))
print("   Function: y = 1 / ( 1 + e^(-{} - {}x))".format(theta0, theta1))

step = np.array(np.arange(0, 20, 1))
ans = 1 / ( 1 + math.e ** ((-1) * theta0 - theta1 * step))
dbvalue = [-theta0/theta1] * 100
dbstep = np.array(np.arange(0, 1, 0.01))
print("   Decision boundary: x = {}".format(dbvalue[0]))

plt.plot(list(step), list(ans), "b-", label = "answer line")
plt.plot(dbvalue, list(dbstep), "y-", label = "decision boundary")
plt.legend(loc='best')
plt.savefig("05_Fig1_DataPlot.pdf")

plt.figure(2)
plt.title("Error Plot")
plt.plot(errorList, "b-")
plt.savefig("05_Fig2_ErrorPlot.pdf")

'''
# Step3. 代价函数图像
print("\n   >>> Step 3 <<<   \n")
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure(3)
ax = fig.gca(projection='3d')

X = np.arange(-2, 0, 0.005)
Y = np.arange(-1, 1, 0.005)
Z = np.zeros((400,400))
print(">> Caculate start!")
for i in range(0, 400):
    print("  Caculating... now is {:3d}/400".format(i))
    for j in range(0, 400):
        J = 0
        for i in range(0, m):
            h = 1.0 / ( 1 + math.e ** (-(X[i] + theta1 * Y[j] )) )
            J = J + y[i] * math.log(h) + (1-y[i]) * math.log(1-h)
        J = J / m * (-1)
        Z[i, j] = J
print(">> Caculate finish!")

X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.title("Cost Function Plot")
plt.savefig("05_Fig3_CostFunctionPlot.pdf")

plt.figure(4)
plt.title("Cost Function Contour Plot")
plt.contour(X, Y, Z)
plt.colorbar()
plt.savefig("05_Fig4_CostFunctionContourPlot.pdf")

plt.show()
'''