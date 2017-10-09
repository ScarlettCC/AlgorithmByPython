#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/4 11:19
# @Author  : Lelsey
# @Site    :
# @File    : colicTest.py
# @Software: PyCharm Community Edition
# @Description: Logistics Regression
from numpy import *

def loadDataSet():
    dataMet = []
    labelMet = []
    with open('testSet.txt') as fr:
        for line in fr.readlines():
            lineArr = line.strip().split()
            dataMet.append([1.0, float(lineArr[0]), float(lineArr[1])])
            labelMet.append(int(lineArr[2]))
    return dataMet, labelMet
def sigmoid(intX):
    return 1.0/(1+exp(-intX))
def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)
    n = dataMatrix.shape[0]
    labeMat = mat(classLabels).transpose()
    m, n = shape(dataMatrix)
    alpha = 0.001       #步长
    maxCycles = 500    #迭代次数
    weights = ones((n, 1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)
        error = (labeMat - h)
        weights += alpha*dataMatrix.transpose()*error
    return weights
def plotBstFit(weights):
    import matplotlib.pyplot as plt
    dataMat, lableMat = loadDataSet()
    dataArr = array(dataMat)
    n = dataArr.shape[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(lableMat[i] == 1):
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2] #令w0*x0 + w1*x1 + w2*x2 = 0，其中x0=1，解出x1和x2的关系
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
def stocGradAscent0(dataMatrix, classLables):
    m,n = shape(dataMatrix)  #shape(dataMatrix) =(100, 3)
    alpha = 0.01
    weights = ones(n)        #shape(weights)=(3,)
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))  #数值
        error = classLables[i] - h
        weights = weights + alpha * error * dataMatrix[i]  #shape(dataMatrix[i])=(3,)， alpha * error * dataMatrix[i]是一个数值
    return weights
def stoGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = shape(dataMatrix)
    weights = ones(n)
    for j in range(numIter):
        dataIndex = range(m)
        #dataIndex = len(range(m))
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.01
            #randIndex = int(random.uniform(0, dataIndex))
            randIndex = random.randint(0, len(dataIndex))   #随机选取样本
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex]-h
            weights += alpha*error*dataMatrix[randIndex]
            del dataIndex[randIndex]   #将已使用的值删除
            #dataIndex -= 1
    return weights

# datamet, labelmet = loadDataSet()
# wei0 = gradAscent(datamet, labelmet)
# plotBstFit(wei0)
# wei1 = stocGradAscent0(array(datamet), labelmet)   #datamet仅是普通list，array(datamet)传入ndarray
# plotBstFit(wei1)
# wei2 = stoGradAscent1(array(datamet), labelmet)
# plotBstFit(wei2)