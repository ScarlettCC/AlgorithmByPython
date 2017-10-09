# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        if A==None or len(A)<=0:
            return B
        former = [1]*len(A)
        back = [1]*len(A)
        for i in range(1,len(A)):
            former[i] = former[i-1]*A[i-1]
        for i in range(len(A)-2,-1,-1):
            back[i] = back[i+1]*A[i+1]
        for i in range(len(A)):
            B.append(back[i]*former[i])
        return B
test = [1, 2, 3, 4]
s = Solution()
print s.multiply(test)