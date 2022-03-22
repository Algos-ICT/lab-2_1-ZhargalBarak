def printOpt(S,i,j):
    global res
    if i == j:
        res += 'A'
    else:
        res += '('
        printOpt(S,i,S[i][j])
        printOpt(S,S[i][j]+1,j)
        res += ')'

m = []
with open('input.txt') as f:
    n = int(f.readline())
    if n % 2 == 1:
        for i in range(n):
            s = list(map(int, f.readline().split()))
            if i % 2 == 0:
                m.append(s[0])
                m.append(s[1])
    else:
        for i in range(n-1):
            s = list(map(int, f.readline().split()))
            if i % 2 == 0:
                m.append(s[0])
                m.append(s[1])
        s = list(map(int, f.readline().split()))
        m.append(s[1])

C = [[0 for i in range(n)] for _ in range(n)]
S = [[0 for i in range(n)] for _ in range(n)]
for i in range(n):
    S[i][i] = i

for s in range(1, n):
    for i in range(n-s):
        j = i+s
        minim = C[i][i] + C[i+1][j] + m[i] * m[i+1] * m[j+1]
        t = i
        for k in range(i+1, j):
            cur = C[i][k] + C[k+1][j] + m[i] * m[k+1] * m[j+1]
            if cur < minim:
                minim = cur
                t = k
        C[i][j] = minim
        S[i][j] = t

res = ''
printOpt(S,0,n-1)
with open('output.txt', 'w') as f:
    f.write(res)
print(int(True))