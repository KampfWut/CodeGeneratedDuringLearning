# Author:   Jin Xu
# Data:     2019-02-13
# Function: Class of Logistic Regression

#--------------------------     import package    --------------------------#

import numpy as np

#---------------------------     main function     ---------------------------#

class logistic(object):
    def __init__(self):
        self.W = None   # 权值theta

    def train(self, X, y, learn_rate = 0.01, lam = 0, num_iters = 5000):
    # 主要程序：
    # 输入： X—系数array，m*n； y—结果array，m*1； learn_rate—学习效率，alpha； lam—正则化系数； num_iters—循环次数
    # 输出： loss_list—误差序列； 通过self.W查看theta系数

        num_train, num_feature = X.shape
        #init the weight
        self.W = 0.001 * np.random.randn(num_feature, 1).reshape((-1, 1))
        loss = [] # 误差序列

        l = np.eye(num_feature)
        l[0, 0] = 0
        L = np.eye(num_feature) - learn_rate * lam * l / num_train
        
        for i in range(num_iters):
            error, dW = self.compute_loss(X, y)
            error = error + lam / num_train * 0.5 * sum(np.square(self.W[1:num_feature]))[0]
            self.W = np.dot(L, self.W) - learn_rate * dW
            
            loss.append(error)
            if i%200 == 0:
                print("   now i = {:5d}, error is {:.6f}".format(i, error))

        return loss
    
    def compute_loss(self, X, y):
        num_train = X.shape[0]
        h = self.output(X)
        loss = -np.sum((y * np.log(h) + (1-y) * np.log((1-h))))
        loss = loss / num_train
        
        dW = X.T.dot((h-y)) / num_train
    
        return loss,dW
    
    def output(self,X):
        g = np.dot(X, self.W)
        return self.sigmod(g)

    def sigmod(self,X):
        return 1/ (1 + np.exp(-X))
    
    def predict(self,X_test):
        h = self.output(X_test)
        y_pred = np.where(h >= 0.5, 1, 0)
        return y_pred

#######################################################