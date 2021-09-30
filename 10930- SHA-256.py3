import hashlib

text = input()

encode_data = text.encode()
answer = hashlib.sha256(encode_data).hexdigest()
print(answer)