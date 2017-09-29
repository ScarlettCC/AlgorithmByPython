# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        i = 0
        for num in pushV:
            stack.append(num)
            while i < len(popV) and popV[i]==stack[-1]:
                stack.pop()
                i += 1
        if len(stack):
            return False
        else:
            return True
pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.IsPopOrder(pushV, popVF))
print(S.IsPopOrder(pushV,popV))