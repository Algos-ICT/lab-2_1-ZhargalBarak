from collections import deque

def dinam(i, j):
    global A, prices
    if i >= 1:
        cost = prices[i-1]
    if j > i:
        return float('inf')
    else:
        if j <= 0:
            if i <= 0:
                return 0
            else:
                if cost <= 100:
                    res = min(dinam(i-1,j+1), dinam(i-1,j) + cost)
                else:
                    return dinam(i-1,j+1)
        else:
            if A[i][j] != -1:
                return A[i][j]
            if cost > 100:
                res = min(dinam(i-1,j+1), dinam(i-1,j-1) + cost)
            else:
                res = min(dinam(i-1,j+1), dinam(i-1,j) + cost)
        A[i][j] = res
        return res

def reconstr(path, i, j):
    if j < i:
        global prices
        if i >= 1:
            cost = prices[i-1]
        if j <= 0:
            if i >= 1:
                if cost > 100:
                    path.append(i)
                    reconstr(path, i-1, j+1)
                else:
                    if dinam(i,j) == dinam(i-1,j+1):
                        path.append(i)
                        reconstr(path, i-1, j+1)
                    else:
                        reconstr(path, i-1, j)
        else:
            if cost <= 100:
                if dinam(i, j) == dinam(i-1, j+1):
                    path.append(i)
                    reconstr(path, i-1, j+1)
                else:
                    reconstr(path, i-1, j)
            else:
                if dinam(i, j) == dinam(i-1, j+1):
                    path.append(i)
                    reconstr(path, i-1, j+1)
                else:
                    reconstr(path, i-1, j-1)


with open('input.txt') as f:
    n = int(f.readline())
    prices = []
    for i in range(n):
        prices.append(int(f.readline()))
A = [[-1 for _ in range(n+2)] for i in range(n+1)]

ans = float('inf')
for i in range(n+1):
    if dinam(n,i) <= ans:
        ans = dinam(n,i)
        k1 = i
path = deque()
reconstr(path, n, k1)

k2 = len(path)
with open('output.txt', 'w') as f:
    f.write(str(ans) + '\n')
    f.write(str(k1) + ' ' + str(k2) + '\n')

    while len(path) > 0:
        f.write(str(path.pop()) + '\n')

