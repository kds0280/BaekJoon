document = input()
word = input()
count = 0
index = 0

#파이썬은 for 문에서 index 변경이 불가해서 while 문으로 대체
while len(document)-len(word)+1> index:
    if document[index:index+len(word)] == word:
        count += 1
        index += len(word)
    else:
        index += 1
print(count)