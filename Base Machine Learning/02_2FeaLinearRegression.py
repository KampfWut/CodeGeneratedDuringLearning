# 02. 双特征线性回归
# 徐进 2019.02.02

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
origal_x = np.array(np.arange(200, 1800, 4))
origal_y = np.array(np.arange(50, 450, 1))
origal_z = 13 + 24 * origal_x + 43 * origal_y
m = len(origal_x)
x, y, z = [], [], []
for i in range(0, m):
    if i % 3 == 0:
        temp = origal_x[i] + rd.randint(-1000, 1000)
    else:
        temp = origal_x[i] + rd.randint(-200, 200) 
    x.append(temp)
for i in range(0, m):
    if i % 3 == 0:
        temp = origal_y[i] + rd.randint(-200, 200)
    else:
        temp = origal_y[i] + rd.randint(-50, 50) 
    y.append(temp)
for i in range(0, m):
    if i % 3 == 0:
        temp = origal_z[i] + rd.randint(-20000, 20000)
    else:
        temp = origal_z[i] + rd.randint(-5000, 5000) 
    z.append(temp)

# Output
print(">> Data: ")
print("   origal_x: {}".format(origal_x[1:10]))
print("   origal_y: {}".format(origal_y[1:10]))
print("   origal_z: {}".format(origal_z[1:10]))
print("   x:        {}".format(x[1:10]))
print("   y:        {}".format(y[1:10]))
print("   z:        {}".format(z[1:10]))
fig = plt.figure(1)
ax = fig.gca(projection='3d')
plt.title("Data Plot")
surf = ax.scatter(x, y, z, "rx", label = "random data")
surf = ax.scatter(origal_x, origal_y, origal_z, "go", label = "origal data")

# Step2. 线性回归
print("\n   >>> Step 2 <<<   \n")

'''
# 特征缩放和归一化
mean_x, mean_y = np.mean(x), np.mean(y)
std_x, std_y = np.std(x, 0), np.std(y, 0)
x = list((np.array(x) - mean_x) / std_x)
y = list((np.array(y) - mean_y) / std_y)

# Output
print("ChangeX: {}".format(x[1:10]))
print("ChangeY: {}".format(y[1:10]))
'''

theta0 = smp.symbols("theta0")
theta1 = smp.symbols("theta1")
theta2 = smp.symbols("theta2")
J = 0
for i in range(0, m):
    J = J + (theta0 + theta1*x[i] + theta2*y[i] - z[i])**2
J = J / (2*m)
DJtheta0 = smp.diff(J, theta0)
DJtheta1 = smp.diff(J, theta1)
DJtheta2 = smp.diff(J, theta2)

# Output
print("Cost function: {}".format(smp.simplify(J)))
print("Diff theta0  : {}".format(smp.simplify(DJtheta0)))
print("Diff theta1  : {}".format(smp.simplify(DJtheta1)))
print("Diff theta2  : {}".format(smp.simplify(DJtheta2)))

alpha = 0.000001
t0, t1, t2 = 0, 0, 0
count = 0
nowJ = J.subs({theta0: t0, theta1: t1, theta2: t2})
subvalue = 9999999999999999999
errorList = []

# MainBody
print(">> Linear Regression Start")
while subvalue > 0.005 and count <= 500:
    count = count + 1
    lastJ = nowJ
    tempt0 = t0 - alpha * DJtheta0.subs({theta0: t0, theta1: t1, theta2: t2})
    tempt1 = t1 - alpha * DJtheta1.subs({theta0: t0, theta1: t1, theta2: t2})
    tempt2 = t2 - alpha * DJtheta2.subs({theta0: t0, theta1: t1, theta2: t2})
    t0, t1, t2 = tempt0, tempt1, tempt2
    nowJ = J.subs({theta0: t0, theta1: t1, theta2: t2})
    subvalue = lastJ - nowJ
    errorList.append(nowJ)
    print("  Count {:3d}: NowJ is {}, Subvalue is {}".format(count, nowJ, subvalue))

# Output
print("\n>> Ans:")
print("   theta0: {}, theta1: {}, theta2: {}".format(t0, t1, t2))
print("   Function: z = {} + {}x + {}y".format(t0, t1, t2))
stepx = np.array(np.arange(-500, 2500, 1))
stepy = np.array(np.arange(-100, 650, 0.25))
ans = t0 + t1 * stepx + t2 * stepy
surf = ax.plot(stepx, stepy, ans, "b-", label = "answer line")
plt.legend(loc='best')
plt.savefig("02_Fig1_DataPlot.pdf")

plt.figure(2)
plt.title("Error Plot")
plt.plot(errorList, "b-")
plt.savefig("02_Fig2_ErrorPlot.pdf")

# Step3. 代价函数图像
print("\n   >>> Step 3 <<<   \n")

fig = plt.figure(3)
ax = fig.gca(projection='3d')

X = np.arange(0, 50, 0.1)
Y = np.arange(0, 100, 0.2)
Z = np.zeros((500,500))
print(">> Caculate start!")
for i in range(0, 500):
    print("  Caculating... now is {:3d}/500".format(i))
    for j in range(0, 500):
        Z[i, j] = J.subs({theta0: 0, theta1: X[i], theta2: Y[j]})
print(">> Caculate finish!")
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.title("Cost Function Plot")
plt.savefig("02_Fig3_CostFunctionPlot.pdf")
 
plt.figure(4)
plt.title("Cost Function Contour Plot")
plt.contour(X, Y, Z)
plt.colorbar()
plt.savefig("02_Fig4_CostFunctionContourPlot.pdf")
