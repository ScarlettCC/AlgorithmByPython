#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/4 11:19
# @Author  : Lelsey
# @Site    : 
# @File    : colicTest.py
# @Software: PyCharm Community Edition
# @Description: 从疝气病症预测病马的死亡率
from LogristicsRegression import *
def classifyVector(intX, weights):
    prob = sigmoid(sum(intX * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0
def colicTest():
    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')
    trainingSet = []
    trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainweights = stoGradAscent1(array(trainingSet), trainingLabels, 500)
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainweights)) != int(currLine[21]):
            errorCount += 1
    errorRate = float(errorCount)/numTestVec
    print "the error rate of this test is:%f" % errorRate
    return errorRate
def multiTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print "after %d iterations the average error rate is: %f" % (numTests, errorSum/float(numTests))

loadDataSet()
multiTest()