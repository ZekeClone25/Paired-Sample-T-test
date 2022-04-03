import statistics as stat
import numpy as np
import matplotlib as matp
import random as ran
import math
import scipy.stats as sstats

class statisticFunc():
    def __init__(self, variableA, variableB, variableC, alpha, tail):
        self.variableA = variableA  # if you want to initialize random elements, just swap it to the ran.sample
        self.variableB = variableB  # if you want to initialize random elements, just swap it to the ran.sample
        self.variableC = variableC
        self.alpha = alpha
        self.tail = tail

    def getVarCValues(self):
        for i in range(len(self.variableA)):
            self.variableC.append(self.variableA[i] - self.variableB[i])
        return self.variableC

    def getSampleMeanDif(self):
        return stat.mean(self.variableC)

    def stdevS(self):
        return stat.stdev(self.variableC)

    def getEstSEM(self):
        return self.stdevS() / math.sqrt(len(self.variableA))

    def getTValue(self):
        return self.getSampleMeanDif() - 0 / self.getEstSEM()
        # in other test, it uses sample mean dif - population mean dif
        # but if you are only testing null hypothesis, just use 0
    def getCritValue(self):
        if self.tail == "left":
            #Use this to identify if the test are statistically significant if T-value < Critical Value
            return sstats.t.ppf(self.alpha, len(self.variableA) - 1)
        elif self.tail == "right":
            #Use this to identify if the test are statistically significant if T-value > Critical Value
            return sstats.t.ppf(1 - self.alpha, len(self.variableA) - 1)
        elif self.tail == "both":
            #Use this to identify if the test are statistically significant if
            # +Critical Value > T-value < -Critical Value
            return sstats.t.ppf(1 - self.alpha / 2, len(self.variableA) - 1)
    def verdict(self):
        if self.tail == "left":
            if self.getTValue() > self.getCritValue():
                return "Null Hypothesis Rejected"
            else:
                return "Null Hypothesis Accepted"
        if self.tail == "right":
            if self.getTValue() < self.getCritValue():
                return "Null Hypothesis Rejected"
            else:
                return "Null Hypothesis Accepted"
        if self.tail == "both":
            if self.getTValue() > -self.getCritValue() and self.getTValue() < self.getCritValue():
                return "Null Hypothesis Rejected"
            else:
                return "Null Hypothesis Accepted"

#lets say you want to compare the pre-test and post-test score of 15 students
#and to test if there is a statistically significant difference to each other
#the test is composed of 40 questionnaires

#two paired data list that have same size, if not, this stuff will not work
variableA = ran.sample(range(1, 40), 15)  # for example only, change it to set of data if you want to try
variableB = ran.sample(range(1, 40), 15)  # for example only, change it to set of data if you want to try
variableC = []
alpha = 0.05 #common alpha value is set to 0.05
tailDesc = "left" #default is set to left one tailed

statsFunc = statisticFunc(variableA, variableB, variableC, alpha, tailDesc)

def printTest():
    # Test if those methods in stats class is working
    print("Difference from VariableB to Variable A: ")
    print(statsFunc.getVarCValues())
    print("Sample Mean Difference: " + str(statsFunc.getSampleMeanDif()))
    print("Sample Standard Deviation of Mean Difference: " + str(statsFunc.stdevS()))
    print("Estimate Standard of Error: " + str(statsFunc.getEstSEM()))
    print("T-value: " + str(statsFunc.getTValue()))
    print("Critical Value (" + str(alpha) + ", " + tailDesc + "): " + str(statsFunc.getCritValue()))
    print("Hypothesis Testing result: " + statsFunc.verdict())
printTest()