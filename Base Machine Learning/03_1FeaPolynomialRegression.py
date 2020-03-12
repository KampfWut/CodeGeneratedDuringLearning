# 03. 单特征多项式回归
# 徐进 2019.02.02

import math
import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt
import sympy as smp

# Step1. 生成数据
print("\n   >>> Step 1 <<<   \n")
origal_x = np.array(range(50, 450))
origal_y = 3 * (origal_x ** 2) + 4 * origal_x + 10
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
        i = i + rd.randint(-40000, 40000)
    else:
        i = i + rd.randint(-10000, 10000) 
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
    print("  Count {:3d}: NowJ is {}, Subvalue is {}".format(count, nowJ, subvalue))

# Output
print("\n>> Line Regreeion Answer:")
print("   theta0: {}, theta1: {}".format(t0, t1))
print("   Function: y = {} + {}x".format(t0, t1))
step = np.array(range(-100, 500))
ans = t0 + t1 * step
plt.plot(list(step), list(ans), "y-", label = "answer 1-dim line")

# Step3. 二次回归
print("\n   >>> Step 3 <<<   \n")
theta0 = smp.symbols("theta0")
theta1 = smp.symbols("theta1")
theta2 = smp.symbols("theta2")
J = 0
for i in range(0, m):
    J = J + (theta0 + theta1*x[i] + theta2*(x[i]**2) - y[i])**2
J = J / (2*m)
DJtheta0 = smp.diff(J, theta0)
DJtheta1 = smp.diff(J, theta1)
DJtheta2 = smp.diff(J, theta2)

# Output
print("Cost function: {}".format(smp.simplify(J)))
print("Diff theta0  : {}".format(smp.simplify(DJtheta0)))
print("Diff theta1  : {}".format(smp.simplify(DJtheta1)))
print("Diff theta2  : {}".format(smp.simplify(DJtheta2)))

alpha = 0.00000000003
t0, t1, t2 = 0, 0, 0
count = 0
nowJ = J.subs({theta0: t0, theta1: t1, theta2: t2})
subvalue = 9999999999999999999

# MainBody
print(">> 2-Dim Regression Start")
while subvalue > 0.05 and count <= 100:
    count = count + 1
    lastJ = nowJ
    tempt0 = t0 - alpha * DJtheta0.subs({theta0: t0, theta1: t1, theta2: t2})
    tempt1 = t1 - alpha * DJtheta1.subs({theta0: t0, theta1: t1, theta2: t2})
    tempt2 = t2 - alpha * DJtheta2.subs({theta0: t0, theta1: t1, theta2: t2})
    t0, t1, t2 = tempt0, tempt1, tempt2
    nowJ = J.subs({theta0: t0, theta1: t1, theta2: t2})
    subvalue = lastJ - nowJ
    print("  Count {:3d}: NowJ is {}, Subvalue is {}".format(count, nowJ, subvalue))

# Output
print("\n>> 2-Dim Regreeion Answer:")
print("   theta0: {}, theta1: {}, theta2: {}".format(t0, t1, t2))
print("   Function: y = {} + {}x + {}x^2".format(t0, t1, t2))
step = np.array(range(-100, 500))
ans = t0 + t1 * step + t2 * (step**2)
plt.plot(list(step), list(ans), "c-", label = "answer 2-dim line")

# Step4. 三次回归
print("\n   >>> Step 4 <<<   \n")
theta0 = smp.symbols("theta0")
theta1 = smp.symbols("theta1")
theta2 = smp.symbols("theta2")
theta3 = smp.symbols("theta3")
J = 0
for i in range(0, m):
    J = J + (theta0 + theta1*x[i] + theta2*(x[i]**2) + theta3*(x[i]**3) - y[i])**2
J = J / (2*m)
DJtheta0 = smp.diff(J, theta0)
DJtheta1 = smp.diff(J, theta1)
DJtheta2 = smp.diff(J, theta2)
DJtheta3 = smp.diff(J, theta3)

# Output
print("Cost function: {}".format(smp.simplify(J)))
print("Diff theta0  : {}".format(smp.simplify(DJtheta0)))
print("Diff theta1  : {}".format(smp.simplify(DJtheta1)))
print("Diff theta2  : {}".format(smp.simplify(DJtheta2)))
print("Diff theta3  : {}".format(smp.simplify(DJtheta3)))

alpha = 0.0000000000000003
t0, t1, t2, t3 = 0, 0, 0, 0
count = 0
nowJ = J.subs({theta0: t0, theta1: t1, theta2: t2, theta3: t3})
subvalue = 9999999999999999999

# MainBody
print(">> 3-Dim Regression Start")
while subvalue > 0.05 and count <= 100:
    count = count + 1
    lastJ = nowJ
    tempt0 = t0 - alpha * DJtheta0.subs({theta0: t0, theta1: t1, theta2: t2, theta3: t3})
    tempt1 = t1 - alpha * DJtheta1.subs({theta0: t0, theta1: t1, theta2: t2, theta3: t3})
    tempt2 = t2 - alpha * DJtheta2.subs({theta0: t0, theta1: t1, theta2: t2, theta3: t3})
    tempt3 = t3 - alpha * DJtheta3.subs({theta0: t0, theta1: t1, theta2: t2, theta3: t3})
    t0, t1, t2, t3 = tempt0, tempt1, tempt2, tempt3
    nowJ = J.subs({theta0: t0, theta1: t1, theta2: t2, theta3: t3})
    subvalue = lastJ - nowJ
    print("  Count {:3d}: NowJ is {}, Subvalue is {}".format(count, nowJ, subvalue))

# Output
print("\n>> 3-Dim Regreeion Answer:")
print("   theta0: {}, theta1: {}, theta2: {}, theta3: {}".format(t0, t1, t2, t3))
print("   Function: y = {} + {}x + {}x^2 + {}x^3".format(t0, t1, t2, t3))
step = np.array(range(-100, 500))
ans = t0 + t1 * step + t2 * (step**2) + t3 * (step**3) 
plt.plot(list(step), list(ans), "m-", label = "answer 3-dim line")
plt.legend(loc='best')
plt.savefig("03_Fig1_DataPlot.pdf")
plt.show()



