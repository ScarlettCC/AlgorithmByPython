import sys
class Solution:
    def xor_solution(self, number, xornumber):
        count = 0
        if number == 0 or xornumber == None:
            return count
        xorlist = []
        xorlist.append(xornumber[0])
        if xornumber[0] == 0 :
            count +=1
        i = 0
        while i<number:
            for x in range(len(xorlist)):
                xorlist[x] = xorlist[x]^xornumber[i]
                if sum(xorlist.count(0))>0:
                    count += xorlist.count(0)
                    xorlist = []
                    xorlist.append(xornumber[i+1])
                    i += 1
            i += 1
        return count
if __name__ == "__main__":
    S = Solution()
    number = sys.stdin.readline
    xornumber = sys.stdin.readline().strip()
    print S.xor_solution(int(number), xornumber)

