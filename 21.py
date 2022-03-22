actions = {'6':['7', '8', '9', 'T', 'J', 'Q', 'K', 'A'],
           '7':['8', '9', 'T', 'J', 'Q', 'K', 'A'],
           '8':['9', 'T', 'J', 'Q', 'K', 'A'],
           '9':['T', 'J', 'Q', 'K', 'A'],
           'T':['J', 'Q', 'K', 'A'],
           'J':['Q', 'K', 'A'],
           'Q':['K', 'A'],
           'K':['A'],
           'A':[None],
           'trump':['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']}

with open('input.txt') as f:
    N, M, R = map(str, f.readline().split())
    my = list(map(str, f.readline().split()))
    enemy = list(map(str, f.readline().split()))
N, M = int(N), int(M)

S = []
C = []
D = []
H = []
for i in range(N):
    if my[i][1] == 'S':
        S.append(my[i][0])
    elif my[i][1] == 'C':
        C.append(my[i][0])
    elif my[i][1] == 'D':
        D.append(my[i][0])
    else:
        H.append(my[i][0])

for i in range(M):
    beaten = False
    suit = enemy[i][1]
    card = enemy[i][0]
    if suit == 'S':
        for j in actions[card]:
            if beaten == False:
                if j in S:
                    S.remove(j)
                    beaten = True
    elif suit == 'C':
        for j in actions[card]:
            if beaten == False:
                if j in C:
                    C.remove(j)
                    beaten = True
    elif suit == 'D':
        for j in actions[card]:
            if beaten == False:
                if j in D:
                    D.remove(j)
                    beaten = True
    else:
        for j in actions[card]:
            if beaten == False:
                if j in H:
                    H.remove(j)
                    beaten = True
    if beaten == False:
        if suit == R:
            with open('output.txt', 'w') as f:
                f.write('NO')
            exit()
        else:
            if R == 'S':
                for j in actions['trump']:
                    if beaten == False:
                        if j in S:
                            S.remove(j)
                            beaten = True
            elif R == 'C':
                for j in actions['trump']:
                    if beaten == False:
                        if j in C:
                            C.remove(j)
                            beaten = True
            elif R == 'D':
                for j in actions['trump']:
                    if beaten == False:
                        if j in D:
                            D.remove(j)
                            beaten = True
            else:
                for j in actions['trump']:
                    if beaten == False:
                        if j in H:
                            H.remove(j)
                            beaten = True
            if beaten == False:
                with open('output.txt', 'w') as f:
                    f.write('NO')
                exit()
with open('output.txt', 'w') as f:
    f.write('YES')