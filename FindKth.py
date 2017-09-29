import sys
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <=0:
            return None
        n = len(tinput)
        start = 0
        end = n - 1
        index = self.Partition(tinput, n, start, end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.Partition(tinput, n, start, end)
            else:
                start = index + 1
                index = self.Partition(tinput, n, start, end)
        output = tinput[len(tinput)-k]
        return output

    def Partition(self, numbers, length, start, end):
        if numbers == None or length <= 0 or start < 0 or end >= length:
            return None
        if end == start:
            return end
        pivotvlue = numbers[start]
        leftmark = start + 1
        rightmark = end

        done = False

        while not done:
            while leftmark <= rightmark and numbers[leftmark] <= pivotvlue :
                leftmark += 1
            while  rightmark >= leftmark and numbers[rightmark] >= pivotvlue:
                rightmark -= 1

            if leftmark > rightmark:
                done = True
            else:
                numbers[leftmark], numbers[rightmark] = numbers[rightmark], numbers[leftmark]
        numbers[rightmark], numbers[start] = numbers[start], numbers[rightmark]
        return rightmark


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    number = sys.stdin.readline().strip().split()
    input = []
    for i in number:
        input.append(int(i))
    k =2
    s = Solution()
    print s.GetLeastNumbers_Solution(input, k)