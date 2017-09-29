class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        return self.select(num, 0, len(num)-1, len(num)/2)

    def partition(self, num, l, r):
        pivot = num[l]
        i = l
        j = r
        while i < j:
            while pivot < num[j] and i < j:
                j -= 1
            if i < j:
                num[i] = num[j]
                i += 1
            while pivot > num[i] and i < j:
                i += 1
            if i < j:
                num[j] = num[i]
                j -= 1
        num[i] = pivot
        return i

    def select(self,num,l,r,k):
        if l == r:
            return num[l]
        i = self.partition(num,l,r)
        j = i - l
        if j == k:
            return num[i]
        if(j < k):
            return self.select(num, i+1, r, k-j-1)
        else:
            return self.select(num,l,i-1,k)

if __name__ == '__main__':
    s = Solution()
    str = raw_input()
    s.majorityElement(list(str))