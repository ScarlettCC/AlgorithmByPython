import sys

class Solution:
    def GetUglyNumber(self, ind):
        if ind == None and len(ind) <= 0:
            return 0
        #print index
        ugly = [1]*ind
        #print ugly
        next = 1

        ind2 = 0
        ind3 = 0
        ind5 = 0

        while next < ind:
            valmin = min(ugly[ind2]*2, ugly[ind3]*3, ugly[ind5]*5)
            ugly[next] = valmin

            while ugly[ind2]*2 <= ugly[next]:
                ind2 = ind2 + 1
            while ugly[ind3]*3 <= ugly[next]:
                ind3 = ind3 + 1
            while ugly[ind5]*5 <= ugly[next]:
                ind5 = ind5 + 1
            next = next + 1
        return ugly[-1]
if __name__ == "__main__":
    S = Solution()
    num = sys.stdin.readline()
    print S.GetUglyNumber(int(num))
