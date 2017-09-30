import sys
class Solution():
    def devideby7(self, n, a):
        count = 0
        if n <= 0 or len(a) <= 0:
            return count
        if n == 1:
            if int(a[0]) % 7 == 0:
                count += 1
            return count
        for i in range(len(a)-1):
            if int(a[i]) % 7 == 0:
                count += 1
            count += self.getnumber(a[i], a[i+1:])
        return count
    def getnumber(self, pre,numbers,):
        count = 0
        for num in numbers:
            if int(pre+num) % 7 == 0:
                count += 1
            if int(num+pre) % 7 == 0:
                count += 1
        return count

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    a = sys.stdin.readline().strip().split()
    s = Solution()
    print s.devideby7(n, a)