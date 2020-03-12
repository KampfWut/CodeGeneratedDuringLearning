# Author:   Jin Xu
# Data:     2019-02-17
# Function: Class of K-Means

#--------------------------     import package    --------------------------#

import numpy as np
import matplotlib.pyplot as plt

#---------------------------     main function     ---------------------------#

class K_means(object):
    def __init__(self):
        self.mu = None      # 聚类中心
        self.label = None   # 分类标签
    
    def Kmeans(self, x, k = 2, limited = 0.01, display_f = 10):
    # 主要步骤
    # 输入：x——训练集， k——聚类个数， limited——结束限制， display_f——显示频率
    # 输出：loss_list——误差序列

        # Step.1 随机化初始值
        num_train, num_feature = x.shape
        self.mu = []
        for i in range(0, k):
            self.mu.append(x[np.random.randint(num_train), :])
        
        finish_flag = False
        loss_list = []
        count = 0

        while finish_flag == False:
            # Step.2 划分类
            self.label = np.zeros(num_train, int)
            for i in range(0, num_train):
                flag, distance = 0, 999999999999
                for j in range(0, k):
                    temp = np.sum(np.square(x[i, :] - self.mu[j]))
                    if temp < distance:
                        distance = temp
                        flag = j
                self.label[i] = flag
            
            # Step.3 移动中心
            add = np.zeros((k, num_feature), float)
            num = np.zeros(k, int)
            for i in range(0, num_train):
                add[self.label[i], :] =  add[self.label[i], :] + x[i, :]
                num[self.label[i]] = num[self.label[i]] + 1

            new_mu = []
            for i in range(0, k):
                new_mu.append(add[i, :] / num[i])
            difference = self.Judge(new_mu, self.mu, k)

            if difference < limited:
                finish_flag = True
            self.mu = new_mu
            loss_list.append(difference)
            count = count + 1
            if count%display_f == 0:
                print("   now count is {:5d}: difference = {:.8f}".format(count, difference))

        return loss_list
        
    def Judge(self, old_mu, new_mu, k):
        add = 0
        for i in range(0, k):
            add = add + np.sum(np.abs(np.square(old_mu[i] - new_mu[i])))
        return add

#######################################################

if __name__ == "__main__":
    c = K_means()
    x = np.array([[1,2],[4,5],[7,4],[3,5],[4,1],[13,15],[16,17],[17,14],[18,20],[19,12]])

    loss = c.Kmeans(x, 2, 0.01, 1)

    plt.figure(1)
    plt.title("Error Plot")
    plt.plot(loss)

    plt.figure(2)
    plt.title("Data Plot")
    count = 0
    for item in c.mu:
        if count == 0:
            plt.plot(item[0], item[1], 'bx')
        else:
            plt.plot(item[0], item[1], 'rx')
        count = count + 1
    
    count = 0
    for i in c.label:
        if i == 0:
            plt.plot(x[count, 0], x[count, 1], 'bo')
        else:
            plt.plot(x[count, 0], x[count, 1], 'ro')
        count = count + 1
    
    plt.show()


    