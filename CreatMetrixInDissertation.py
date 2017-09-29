# -*-coding:utf-8 -*-
class CreatMetrixInDissertation:
    def creatmetrix(self):
        weight = 1
        printmetrix=[]
        with open("adj200-1.txt") as f:
            strfile = f.read()
            for x in strfile:
                if x == "\n":
                    number = 1
                    printmetrix.append("\n")
                else:
                    printmetrix.append(x*number*5+" ")
                    weight += 1
        with open('dismetrix.txt','w') as dismetrix:
            dismetrix.write(printmetrix)

s=CreatMetrixInDissertation()
s.creatmetrix()
