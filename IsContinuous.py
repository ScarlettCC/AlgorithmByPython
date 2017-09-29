# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if( len(numbers) == 0 or numbers == None):
            return False
        transDict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(len(numbers)):
            if numbers[i] in transDict.keys():
                numbers[i] = transDict[numbers[i]]
        numbers = sorted(numbers)
        numbersofzero = numbers.count(0)
        numbersofGap = 0
        for i in range(numbersofzero,len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                return False
            numbersofGap += numbers[i+1]-numbers[i]-1
        return False if numbersofGap > numbersofzero else True
test = ['A', 3, 2, 5, 0]
test2 = [0, 3, 1, 6, 4]
s = Solution()
print s.IsContinuous(test)
print s.IsContinuous(test2)