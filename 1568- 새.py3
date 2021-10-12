bird = int(input())
count = 0

#새가 0마리 남을 때까지
while bird > 0:
    sing = 1
    #새가 노래보다 더 많을 때까지
    while bird >= sing:
        bird -= sing
        sing += 1
        count += 1
print(count)