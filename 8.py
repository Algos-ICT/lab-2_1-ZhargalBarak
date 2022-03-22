import random

def randomized_quick_sort(A, f, l):
    if f < l:
        k = random.randint(f, l)
        A[f], A[k] = A[k], A[f]
        m1, m2 = part3(A, f, l)
        randomized_quick_sort(A, f, m1-1)
        randomized_quick_sort_2(A, m1, m2)
        randomized_quick_sort(A, m2+1, l)

def part3(A, f, l):
    cur = A[f][0]
    left = []
    mid = []
    right = []
    j = 0
    count = 0
    for i in range(f, l+1):
        if A[i][0] < cur:
            left.append(A[i])
            j += 1
        elif A[i][0] == cur:
            mid.append(A[i])
            count += 1
        else:
            right.append(A[i])
    A[f:l+1] = left + mid + right
    return f+j, f+j+count-1

def randomized_quick_sort_2(A, f, l):
    if f < l:
        k = random.randint(f, l)
        A[f], A[k] = A[k], A[f]
        m1, m2 = part3_2(A, f, l)
        randomized_quick_sort_2(A, f, m1-1)
        randomized_quick_sort_2(A, m2+1, l)

def part3_2(A, f, l):
    cur = A[f][1]
    left = []
    mid = []
    right = []
    j = 0
    count = 0
    for i in range(f, l+1):
        if A[i][1] < cur:
            left.append(A[i])
            j += 1
        elif A[i][1] == cur:
            mid.append(A[i])
            count += 1
        else:
            right.append(A[i])
    A[f:l+1] = left + mid + right
    return f+j, f+j+count-1

lects = []
with open('input.txt') as f:
    N = int(f.readline())
    for _ in range(N):
        lects.append(list(map(int, f.readline().split())))
randomized_quick_sort(lects, 0, N-1)

count = 1
prev = lects[0]
for i in range(1, N):
    if lects[i][0] > prev[0]:
        if lects[i][1] <= prev[1]:
            prev = lects[i]
        elif lects[i][0] >= prev[0]:
            count += 1
            prev = lects[i]

with open('output.txt', 'w') as f:
    f.write(str(count))
