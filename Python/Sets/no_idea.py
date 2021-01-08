n, m = input().split()

arr = input().split()

A = set(input().split())
B = set(input().split())

happiness = 0
sad = 0
for i in arr:
    if i in A:
        happiness+= 1
    if i in B:
        sad+= 1
print(happiness-sad)
