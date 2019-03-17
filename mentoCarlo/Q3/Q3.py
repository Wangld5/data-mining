import numpy as np
import matplotlib.pyplot as plt
import math
import random
import csv

def ff(x, y):
    return (pow(y, 2) * math.exp(-pow(y, 2)) + pow(x, 4) * math.exp(-pow(x, 2))) / (x * math.exp(-pow(x, 2)))

def monteCarlo(n):
    sum = 0
    # for i in range(n):
    #     x = random.random() * 2 + 2
    #     y = random.random() * 2 - 1
    #     z = ff(x, y)
    #     sum = sum + (4 - 2) * (1 - (-1)) * z
    x = np.random.uniform(0,1,n)*2+2
    y = np.random.uniform(0,1,n)*2-1
    z = ff(x, y)
    for i in z:
        sum = sum + i
    
    
    return sum/n

def loopMC(n):
    result = []
    for i in range(100):
        temp_result = monteCarlo(n)
        result.append(temp_result)
    
    the_mean = round(np.mean(result), 4)
    the_variance = round(np.var(result), 4)
    return the_mean, the_variance

if __name__ == "__main__":
    result_mean = []
    result_varience = []
    allParameter = [10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 500]
    csv_file = open("result.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(['number of points', 'mean', 'variance'])
    for i in range(len(allParameter)):
        temp1, temp2 = loopMC(allParameter[i])
        result_mean.append(temp1)
        result_varience.append(temp2)
        row = [allParameter[i], temp1, temp2]
        writer.writerow(row)
    
    #均值曲线图
    rects=plt.bar(range(len(result_mean)), result_mean, color='rgby')
    # X轴标题
    index = [0,1,2,3,4,5,6,7,8,9,10]
    index=[float(c)+0.4 for c in index]
    plt.ylim(ymax=130000, ymin=0)
    plt.xticks(index, allParameter)
    plt.xlabel("sample number") #X轴标签
    plt.ylabel("mean")
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
    plt.show()
    #方差直方图
    rects=plt.bar(range(len(result_varience)), result_varience, color='rgby')
    # X轴标题
    index = [0,1,2,3,4,5,6,7,8,9,10]
    index=[float(c)+0.4 for c in index]
    plt.ylim(ymax=17713431000, ymin=0)
    plt.xticks(index, allParameter)
    plt.xlabel("sample number")
    plt.ylabel("variance") #X轴标签
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
    plt.show()
    csv_file.close()





