import copy

with open('input.txt') as f:
    N = int(f.readline())
prev = [4, 2, 1, 0]
cur = [0 for _ in range(4)]

if N == 1:
    res = 8
else:
    for i in range(N-1):
        cur[0] += prev[1] * 2 + prev[2] * 2
        cur[1] += prev[0] + prev[3] * 2
        cur[2] += prev[0]
        cur[3] += prev[1]
        prev = copy.copy(cur)
        cur = [0 for _ in range(4)]
    res = sum(prev) % 10 ** 9
with open('output.txt', 'w') as f:
    f.write(str(res))

