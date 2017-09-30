import sys
if __name__ == "__main__":
    path = sys.stdin.readline().strip().split('/')
    path_stack = []
    path_res = ''
    dict = ['','.','..']
    for i in path:
        if i not in dict:
            path_stack.append(i)
        if '..'==i and path_stack:
            path_stack.pop(-1)
    if len(path_stack) == 0:
        path_res = '/'
    else:
        for i in path_stack:
            path_res += '/'+i+''
    print path_res