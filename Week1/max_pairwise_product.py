# python3
# Uses python3
n = int(input())
a = sorted([int(x) for x in input().split()])
assert(len(a) == n)

# result = 0

# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

result = a[-1]*a[-2]

# result = 0
# result = [a[i]*a[j] for j in range(i+1,n) for i in range(0,n) if a[i]*a[j]>0]
print(result)
