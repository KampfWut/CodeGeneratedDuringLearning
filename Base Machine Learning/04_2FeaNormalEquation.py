# 04. 正规方程方法
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

# Step.2 数据处理
print("\n   >>> Step 2 <<<   \n")
X = []
for i in range(0, m):
    temp = [1]
    temp.append(x[i])
    temp.append(y[i])
    X.append(temp)
X = np.matrix(X)
Y = np.matrix(z).T

# Step.3 计算
theta = (X.T * X).I * X.T * Y

# Output
print(">> Normal Equation Answer:")
print("   theta0: {}, theta1: {}, theta2: {}".format(theta[0, 0], theta[1, 0], theta[2, 0]))
print("   Function: z = {} + {}x + {}y".format(theta[0, 0], theta[1, 0], theta[2, 0]))
stepx = np.array(np.arange(-500, 2500, 1))
stepy = np.array(np.arange(-100, 650, 0.25))
ans = theta[0, 0] + theta[1, 0] * stepx + theta[2, 0] * stepy
surf = ax.plot(stepx, stepy, ans, "b-", label = "answer line")
plt.legend(loc='best')
plt.savefig("04_Fig1_DataPlot.pdf")
plt.show()

