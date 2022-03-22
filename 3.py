with open('input.txt') as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
    b = list(map(int, f.readline().split()))
a.sort()
b.sort()

sum = 0
for i in range(n):
    sum += a[i] * b[i]

with open('output.txt', 'w') as f:
    f.write(str(sum))

