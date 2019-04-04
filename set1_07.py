num = int(input())

bytes = 0

while num & num-1:
    num -= 1
    bytes += 1

print(bytes)
