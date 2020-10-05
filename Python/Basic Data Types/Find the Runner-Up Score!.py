if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(sorted(set(arr))[-2])

'''
---without set(), sort()---

i = int(input())
arr = list(map(int,raw_input().strip().split()))[:i]
maximim = max(arr)
while max(arr) == maximum:
    arr.remove(max(arr))

print max(arr)

'''   
