def almost_palindrom(s):
    global K
    changes = 0
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            changes += 1
        if changes > K:
            return False
    return True

with open('input.txt') as f:
    N, K = map(int, f.readline().split())
    S = f.readline()

res = N
for i in range(N):
    ind_left = i
    ind_right = i + 2
    flag1 = True
    flag2 = True
    while ind_left >= 0 and ind_right <= N:
        if flag1 and almost_palindrom(S[ind_left - 1:ind_right]) and ind_left - 1 >= 0:
            res += 1
        else:
            flag1 = False
        if flag2 and almost_palindrom(S[ind_left:ind_right]):
            res += 1
        else:
            flag2 = False
        if flag1 == False and flag2 == False:
            break
        ind_left -= 1
        ind_right += 1

with open('output.txt', 'w') as f:
    f.write(str(res))