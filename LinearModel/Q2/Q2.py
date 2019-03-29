import numpy as np
import pandas as pd
from pandas import *
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

##归一化
def normalize(row_num, matrix):
    after = zeros((row_num, 3), dtype=float)
    for i in range(0,3):
        m = np.mean(matrix[:, i])
        mx = max(matrix[:, i])
        mn = min(matrix[:, i])
        after[:, i] = [(float(j) - m) / (mx - mn) for j in matrix[:, i]]
    return after
## 读取文件内容
def readFile(row_num, fileName):
    train = zeros((row_num,3),dtype=float)
    f = open(fileName)
    lines = f.readlines()
    row = 0
    for line in lines:
        list = line.strip('\n').split(' ')
        train[row :] = list[0:3]
        row+=1
    return train

def GradientDescent(maxiter,x,y,theta,alpha, m, testX, testY):
    TrainLoss = []
    TestLoss = []
    xTrains = x.transpose()
    count = 1
    for i in range(0,maxiter):
        hypothesis = np.dot(x,theta)
        loss = (hypothesis-y)
        gradient = np.dot(xTrains,loss)/m
        theta = theta - alpha * gradient
        if(count == 100000):
            TrainLoss.append(1.0/2*m*np.sum(np.square(np.dot(x,np.transpose(theta))-y)))
            TestLoss.append(1.0/2*m*np.sum(np.square(np.dot(testX,np.transpose(theta))-testY)))
            count = 0
        count += 1
    return theta, TrainLoss, TestLoss

if __name__ == "__main__":
    TestArrayB = readFile(10, '..\dataForTesting.txt')
    TrainArrayB = readFile(50, '..\dataForTraining.txt')

    TestArray = normalize(10, TestArrayB)
    TrainArray = normalize(50, TrainArrayB)

    m, n = np.shape(TrainArray)
    x_data = np.ones((m, n))
    x_data[:, :-1] = TrainArray[:, :-1]
    y_data = TrainArray[:, -1]

    M,N = np.shape(TestArray)
    test_x_data = np.ones((M, N))
    test_x_data[:,:-1] = TestArray[:, :-1]
    test_y_data = TestArray[:, -1]

    theta = np.zeros(n)
    result_theta, TrainLoss, TestLoss = GradientDescent(1500000, x_data, y_data, theta, 0.0002, m, test_x_data, test_y_data)
    print(result_theta)
    ## paint
    x = [x/100000 for x in range(1, 1500001) if x%100000 == 0]
    plt.plot(x, TrainLoss, label="trainLoss")
    plt.plot(x, TestLoss, label="testLoss")
    plt.legend()
    plt.show()






    
