import sys
class Solution():
    def dengpao(self,n, state):
        if int(state[len(state)-1]) == 1:
            return 'Alice'
        else:
            return 'Bob'
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    state = sys.stdin.readline().strip().split()
    s = Solution()
    print s.dengpao(n,state)