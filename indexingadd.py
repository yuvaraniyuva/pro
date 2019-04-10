nq = input().split()
num = int(nq[0])
qr = int(nq[1])

in_nums = list(map(int, input().split()))

for _ in range(qr):
    u, v = map(int, input().split())
    st = sum(in_nums[u-1:v])
    print(st)
