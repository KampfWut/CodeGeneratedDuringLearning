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
theta0 = smp.symbols("theta0")
theta1 = smp.symbols("theta1")
J = 0
for i in range(0, m):
    h = 1.0 / ( 1 + smp.E ** (-(theta0 + theta1 * x[i] )) )
    J = J + y[i] * smp.log(h) + (1-y[i]) * smp.log(1-h)
J = J / m * (-1)
DJtheta0 = smp.diff(J, theta0)
DJtheta1 = smp.diff(J, theta1)

alpha = 0.003
t0, t1 = 1, 1
count = 0
nowJ = J.subs({theta0: t0, theta1: t1}).evalf()
subvalue = 9999999999999999999
errorList = []

# MainBody
print(">> Logistic Regression Start")
while count <= 100:
    count = count + 1
    lastJ = nowJ
    tempt0 = t0 - alpha * DJtheta0.subs({theta0: t0, theta1: t1})
    tempt1 = t1 - alpha * DJtheta1.subs({theta0: t0, theta1: t1})
    t0, t1 = tempt0, tempt1
    nowJ = J.subs({theta0: t0, theta1: t1}).evalf()
    subvalue = lastJ - nowJ
    errorList.append(nowJ)
    print("  Count {:3d}: NowJ is {}, Subvalue is {}".format(count, nowJ, subvalue))

# Output
print("\n>> Ans:")
print("   theta0: {}, theta1: {}".format(t0, t1))
print("   Function: y = 1 / ( 1 + e^(-{} - {}x))".format(t0, t1))

step = np.array(np.arange(0, 100, 1))
ans = 1 / ( 1 + math.e ** ((-1) * t0 - t1 * step))
dbvalue = [-t0/t1] * 100
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

plt.show()
