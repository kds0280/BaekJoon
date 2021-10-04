L_length = int(input())
L = []

for i in range(L_length):
    L.append(int(input()))

for i in range(len(L)-1):
  if L[i] > L[i+1]:
    L[i], L[i+1] = L[i+1], L[i]
    if i > 0:
        for i in range(i, 0, -1):
            if L[i-1] > L[i]:
                L[i], L[i-1] = L[i-1], L[i]
for i in L:
    print(i)