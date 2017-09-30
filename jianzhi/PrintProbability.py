class Solution():
    max_value = 6
    def  PrintProbability(self,n):
        if(n==0):
            return 0
        for i in range(n, 6*n+1):
            print i
            print self.probability_core(n,i)

    def probability_core(self, n, sum):
        number = 0
        if(sum < n or sum > 6*n):
            return 0
        if(n == 1):
            return 1
        else:
            for i in range(1, self.max_value+1):
                number += self.probability_core(n-1,sum-i)
            return number

s = Solution()
s.PrintProbability(6 )