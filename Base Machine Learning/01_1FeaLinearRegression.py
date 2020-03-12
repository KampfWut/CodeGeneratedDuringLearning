# 01. 基础单特征线性回归
# 徐进 2019.02.01

import math
import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt
import sympy as smp

# Step1. 生成数据
print("\n   >>> Step 1 <<<   \n")
origal_x = np.array(range(50, 450))
origal_y = 16 * origal_x + 10
m = len(origal_x)
x = []
y = []
for i in origal_x:
    if i % 3 == 0:
        i = i + rd.randint(-200, 200)
    else:
        i = i + rd.randint(-50, 50) 
    x.append(i)
for i in origal_y:
    if (i-10)/16 % 3 == 0:
        i = i + rd.randint(-4000, 4000)
    else:
        i = i + rd.randint(-1000, 1000) 
    y.append(i)

# Output
print(">> Data: ")
print("   origal_x: {}".format(origal_x[1:10]))
print("   origal_y: {}".format(origal_y[1:10]))
print("   x:        {}".format(x[1:10]))
print("   y:        {}".format(y[1:10]))
plt.figure(1)
plt.title("Data Plot")
plt.plot(origal_x, origal_y, "go", label = "origal data")
plt.plot(x, y, "rx", label = "random data")

# Step2. 线性回归
print("\n   >>> Step 2 <<<   \n")
theta0 = smp.symbols("theta0")
theta1 = smp.symbols("theta1")
J = 0
for i in range(0, m):
    J = J + (theta0 + theta1*x[i] - y[i])**2
J = J / (2*m)
DJtheta0 = smp.diff(J, theta0)
DJtheta1 = smp.diff(J, theta1)

# Output
print("Cost function: {}".format(smp.simplify(J)))
print("Diff theta0  : {}".format(smp.simplify(DJtheta0)))
print("Diff theta1  : {}".format(smp.simplify(DJtheta1)))

alpha = 0.000003
t0, t1 = 0, 0
count = 0
nowJ = J.subs({theta0: t0, theta1: t1})
subvalue = 9999999999999999999
errorList = []

# MainBody
print(">> Linear Regression Start")
while subvalue > 0.05 and count <= 100:
    count = count + 1
    lastJ = nowJ
    tempt0 = t0 - alpha * DJtheta0.subs({theta0: t0, theta1: t1})
    tempt1 = t1 - alpha * DJtheta1.subs({theta0: t0, theta1: t1})
    t0, t1 = tempt0, tempt1
    nowJ = J.subs({theta0: t0, theta1: t1})
    subvalue = lastJ - nowJ
    errorList.append(nowJ)
    print("  Count {:3d}: NowJ is {}, Subvalue is {}".format(count, nowJ, subvalue))

# Output
print("\n>> Ans:")
print("   theta0: {}, theta1: {}".format(t0, t1))
print("   Function: y = {} + {}x".format(t0, t1))
step = np.array(range(-100, 700))
ans = t0 + t1 * step
plt.plot(list(step), list(ans), "b-", label = "answer line")
plt.legend(loc='best')
plt.savefig("01_Fig1_DataPlot.pdf")
plt.figure(2)
plt.title("Error Plot")
plt.plot(errorList, "b-")
plt.savefig("01_Fig2_ErrorPlot.pdf")

# Step3. 代价函数图像
print("\n   >>> Step 3 <<<   \n")
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure(3)
ax = fig.gca(projection='3d')

X = np.arange(-5, 5, 0.05)
Y = np.arange(0, 20, 0.1)
Z = np.zeros((200,200))
print(">> Caculate start!")
for i in range(0, 200):
    print("  Caculating... now is {:3d}/200".format(i))
    for j in range(0, 200):
        Z[i, j] = J.subs({theta0: X[i], theta1: Y[j]})
print(">> Caculate finish!")
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.title("Cost Function Plot")
plt.savefig("01_Fig3_CostFunctionPlot.pdf")

plt.figure(4)
plt.title("Cost Function Contour Plot")
plt.contour(X, Y, Z)
plt.colorbar()
plt.savefig("01_Fig4_CostFunctionContourPlot.pdf")