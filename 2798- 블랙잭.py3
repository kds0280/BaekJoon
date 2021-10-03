length, m = list(map(int, input().split(" ")))
num = list(map(int, input().split(" ")))
answer = 0
for i in range(len(num)-2):
    for j in range(i+1, len(num)-1):
        for q in range(j+1, len(num)):
            a = num[i]+num[j]+num[q]
            if a <= m:
                answer = max(answer, a)
print(answer)
           