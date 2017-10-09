# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers == None:
            return duplication
        minnum = len(numbers)
        for i in numbers:
            if i<0 or i>len(numbers)-1:
                return False
        for i in range(0, len(numbers)):
            index = numbers[i]
            if index >= minnum:
                index -= minnum
            if numbers[index] >= minnum:
                duplication[0] = index
                return True
            elif numbers[index]<minnum:
                numbers[index] += minnum
    def duplicate2(self, numbers, duplication):
        if numbers==None :
            return False
        for i in range(len(numbers)):
            while numbers[i]!=i:
                if numbers[i]==numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]
        return False
test = [2, 3, 1, 0, 2, 5, 3]
s = Solution()
dupulication = [0]
#print(s.duplicate(test,dupulication))
#print dupulication[0]
#print(s.duplicate2(test))
print (s.duplicate2(test,dupulication))
print dupulication[0]
