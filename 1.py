import random

def randomized_quick_sort(A, f, l):
    if f < l:
        k = random.randint(f, l)
        A[f], A[k] = A[k], A[f]
        m1, m2 = part3(A, f, l)
        randomized_quick_sort(A, f, m1-1)
        randomized_quick_sort(A, m2+1, l)

def part3(A, f, l):
    cur = A[f][0]/A[f][1]
    left = []
    mid = []
    right = []
    j = 0
    count = 0
    for i in range(f, l+1):
        if A[i][0]/A[i][1] > cur:
            left.append(A[i])
            j += 1
        elif A[i][0]/A[i][1] == cur:
            mid.append(A[i])
            count += 1
        else:
            right.append(A[i])
    A[f:l+1] = left + mid + right
    return f+j, f+j+count-1

def Knapsack(W, pw, n):
    value = 0
    for i in range(n):
        if W == 0:
            return value
        a = min(pw[i][1], W)
        value += pw[i][0]/pw[i][1]*a
        W -= a
    return value

pw = []
with open('input.txt') as f:
    n, W = map(int, f.readline().split())
    for _ in range(n):
        pw.append(list(map(int, f.readline().split())))

randomized_quick_sort(pw, 0, n-1)

with open('output.txt', 'w') as f:
    f.write(str(Knapsack(W, pw, n)))

