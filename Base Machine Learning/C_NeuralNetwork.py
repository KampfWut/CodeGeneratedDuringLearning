# Author:   Jin Xu
# Data:     2019-02-15
# Function: Class of Neural Network

#--------------------------     import package    --------------------------#

import numpy as np
import matplotlib.pyplot as plt

#---------------------------     main function     ---------------------------#

class neuralnetwork(object):
    def __init__(self):
        self.W = None   # theta

    def sigmod(self, X):
        return 1/ (1 + np.exp(-X))
    
    def datachange(self, X, num_train):
        newX = []
        for i in range(0, num_train):
            temp = [1]
            temp.extend(list(X[i]))
            newX.append(temp)
        newX = np.array(newX)
        return newX

    def forward_propagation(self, X, W, layer_num):
        Z, a = [], []
        count = 0
        while count < layer_num - 1:
            if count == 0:
                Z.append(np.dot(X, W[0]))
                a.append(self.datachange(self.sigmod(Z[0]), num_train))
            elif count == layer_num - 2:
                Z.append(np.dot(a[count-1], W[count]))
                H = self.sigmod(Z[count])
                a.append(H)
            else:
                Z.append(np.dot(a[count-1],  W[count]))
                a.append(self.datachange(self.sigmod(Z[count]), num_train))
            count = count + 1
        return Z, a, H
    
    def backward_propagation(self, X, y, layer_num, a, Z, H, lam):
        t = []
        count = layer_num - 1
        num = 0
        while count > 0:
            if count == layer_num - 1:
                t.append(H - y)
            else:
                t.append( np.dot(t[num-1], self.W[count][1:,:].T) * self.sigmod(Z[count-1]) * (1-self.sigmod(Z[count-1])) )
            num = num + 1
            count = count - 1
        T = []
        num = layer_num - 1
        for i in range(0, layer_num - 1):
            if i == 0:
                T.append(np.dot(X.T, t[num-1]))
            else:
                T.append(np.dot(a[i-1].T, t[num-1]))
            num = num - 1    
        D = []
        for i in range(0, layer_num - 1):
            a,b = T[i].shape
            l = np.ones((a,b), int)
            l[0,:] = 0
            l = self.W[i] * l * lam
            D.append(T[i] / num_train + l)
        return D
    
    def calculate_cost(self, y, H, num_train, lam):
        error = - np.sum(y * np.log(H) +  (1-y) * np.log((1-H)) ) / num_train
        wsum = 0
        for item in self.W:
            wsum = wsum + np.sum(item[:, 1:])
        error = error + 0.5 * lam * wsum / num_train
        return error

    def train(self, x, y, layer_num, layer_unit, gradient_test = 0.0001, learn_rate = 0.01, lam = 0, num_iters = 5000):
    # 主要程序：
    # 输入： x—系数array，m*n； y—结果array，m*k； learn_rate—学习效率，alpha； lam—正则化系数； num_iters—循环次数
    # 输出： loss_list—误差序列； 通过self.W查看theta系数

        num_train, num_feature = x.shape
        num_train, num_output = y.shape
        loss_list = []

        # 0. 数据处理
        X = self.datachange(x, num_train)
        if gradient_test != 0:
            num_iters = 1

        # 1. 随机初始值
        self.W = []
        for i in range(0, layer_num-1):
            newW = np.random.rand((layer_unit[i]+1) * layer_unit[i+1], 1).reshape(layer_unit[i]+1, layer_unit[i+1]) * 2 - 1
            self.W.append(newW)
        
        for total_count in range(0, num_iters):
            # 2. 正向传播
            Z, a, H = self.forward_propagation(X, self.W, layer_num)

            # 3. 代价函数
            error = self.calculate_cost(y, H, num_train, lam)
            loss_list.append(error)
            
            # 4. 反向传播
            D = self.backward_propagation(X, y, layer_num, a, Z, H, lam)
            
            # 5. 梯度检查
            if gradient_test != 0:
                print(">>> Do gradient test, test_coefficient = {}".format(gradient_test))
                difference_list = []
                for k in range(0, layer_num - 1):
                    print("")
                    a,b = self.W[k].shape
                    for i in range(0, a):
                        for j in range(0, b):
                            temp_add, temp_subtraction = self.W, self.W
                            temp_add[k][i,j] = temp_add[k][i,j] + gradient_test
                            temp_subtraction[k][i,j] = temp_subtraction[k][i,j] - gradient_test
                            temp1, temp2, H1 = self.forward_propagation(X, temp_add, layer_num)
                            temp1, temp2, H2 = self.forward_propagation(X, temp_subtraction, layer_num)
                            test_value = 0.5 * (self.calculate_cost(y, H1, num_train, lam) - self.calculate_cost(y, H2, num_train, lam)) / gradient_test
                            print("    For Layer {}[{}, {}] --- D = {:.10f}, test_value = {:.10f} --- difference_value = {:.10f}".format(k, i, j, D[k][i,j], test_value, D[k][i,j] - test_value))
                            difference_list.append(abs(D[k][i,j] - test_value))
                print("\n    max difference value = {}".format(max(difference_list)))
            
            # 6. 梯度下降
            for i in range(0, layer_num - 1):
                self.W[i] = self.W[i] - D[i] * learn_rate

            if total_count%200 == 0 and total_count != 0:
                print("   now total_count = {:5d}, error is {:.8f}".format(total_count, error))
        
        return loss_list
        
#######################################################

if __name__ == "__main__":
    c = neuralnetwork()
    x = np.array([[10,20],[30,40],[50,60],[70,80],[90,100]])
    y = np.array([[0, 1], [0, 1], [1, 0], [1, 0], [1, 0]])
    num_train, num_feature = x.shape
    num_train, num_output = y.shape

    loss = c.train(x, y , 4, [num_feature, 3, 4, num_output], 0.001, 0.01, 0, 5000)
    '''
    plt.figure(1)
    plt.title("Error Plot")
    plt.plot(loss)
    plt.xlabel('Iteration number')
    plt.ylabel('Loss value')
    plt.show()
    '''
    

