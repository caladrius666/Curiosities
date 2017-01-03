N = int(input())
S = []
for i in range(N):
    S.append(list(map(float, input().split())))
for i in range(len(S)):
    S[i][0], S[i][1] = S[i][1], S[i][0]
S.sort()
for x in range(N):
    for i in range(N-1):
        if S[i][0] == S[i+1][0]:
            if S[i][1] < S[i+1][1]:
                S[i][1], S[i+1][1] = S[i+1][1], S[i][1]
for i in range(N):
    print((str(round(S[i][1], 2))[:str(round(S[i][1], 2)).index('.')]+(str(round(S[i][1], 2))+'00000000')[str(round(S[i][1], 2)).index('.'):str(round(S[i][1], 2)).index('.')+3]),(str(round(S[i][0], 3))[:str(round(S[i][0], 3)).index('.')]+(str(round(S[i][0], 3))+'00000000')[str(round(S[i][0], 3)).index('.'):str(round(S[i][0], 3)).index('.')+4]))

