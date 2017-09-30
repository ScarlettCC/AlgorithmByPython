import sys

class solution():
    # def numberOfTriangle(self, n, nodes):
    #     numbers = 0
    #     for i in range(n-1):
    #         for j in range(i+1, n-1):
    #             if abs((nodes[j]-nodes[i])/2.0) > 90 and abs((nodes[j]-nodes[i])/2.0) < 180:
    #                 numbers += 1
    #     return numbers
    def numberOfTriangle(self, n, nodes):
        numbers = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for z in range(j+1, n):
                    if abs(nodes[z]-nodes[i]) < 180:
                        numbers += 1
        return numbers
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nodes = [float(sys.stdin.readline().strip()) for i in range(n)]
    s= solution()
    print s.numberOfTriangle(n, nodes)