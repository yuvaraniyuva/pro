n = int(input())
input_strs = []

for _ in range(n):
    input_strs.append(input())

input_zip = list(zip(*input_strs))

result = []
for t in input_zip:
    if all(tt == t[0] for tt in t):
        result.append(t[0])
    else:
        break

print(''.join(result))
