# -*- coding:utf-8 -*-
from datetime import datetime

class Solution():
    '''
    输入多行日期： 年 月 日
    输出：  日期为该年的第几天
    AC！
    '''
    def calculateDay(self, dayStr):
        year= int(dayStr[0])
        month = int(dayStr[1])
        day = int(dayStr[2])
        #调用系统函数实现
        #return datetime(year, month, day).strftime("%j")
        #自己实现
        monthnumber1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthnumber2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.leap(year):
            return self.addDayNumber(monthnumber1, month, day)
        else:
            return self.addDayNumber(monthnumber2, month, day)

    def leap(self,year):
        return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
    def addDayNumber(self, monthnumber, month, day):
        daynumber = 0
        for i in range(month-1):
            daynumber += monthnumber[i]
        daynumber += day
        return daynumber

if __name__ == "__main__":
    number = []
    s = Solution()
    while True:
        try:
            dayStr = raw_input().split()
            number.append(s.calculateDay(dayStr))
        except:
            break
    for i in number:
        print i