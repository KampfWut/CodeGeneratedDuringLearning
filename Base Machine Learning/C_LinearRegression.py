# Author:   Jin Xu
# Data:     2019-02-13
# Function: Class of Linear Regression

#--------------------------     import package    --------------------------#

import numpy as np

#---------------------------     main function     ---------------------------#

class linear(object):
    def __init__(self):
        self.W = None # 权值
    
    def loss(self, X, y):
        num_feature = X.shape[1]
        num_train = X.shape[0]
        
        h = X.dot(self.W)
        loss = 0.5 * np.sum(np.square(h - y)) / num_train
        
        dW = X.T.dot((h-y)) / num_train
        
        return loss, dW
        
    def train(self, X, y, learn_rate = 0.001, lam = 0, iters = 10000):
    # 主要程序：
    # 输入： X—系数array，m*n； y—结果array，m*1； learn_rate—学习效率，alpha； lam—正则化系数； iters—循环次数
    # 输出： loss_list—误差序列； 通过self.W查看theta系数

        num_feature = X.shape[1]
        num_train = X.shape[0]
        self.W = np.zeros((num_feature, 1))
        loss_list = []
        
        l = np.eye(num_feature)
        l[0, 0] = 0
        L = np.eye(num_feature) - learn_rate * lam * l / num_train
        
        for i in range(iters):
            error, dW = self.loss(X, y)
            error = error + lam / num_train * 0.5 * sum(np.square(self.W[1:num_feature]))[0]
            loss_list.append(error)
            self.W = np.dot(L, self.W) - learn_rate * dW
            
            if i%200 == 0:
                print("   now i = {:5d}, error is {:.6f}".format(i, error))

        return loss_list
        
    def predict(self, X_test):
        y_pred = X_test.dot(self.W)
        return y_pred

#######################################################