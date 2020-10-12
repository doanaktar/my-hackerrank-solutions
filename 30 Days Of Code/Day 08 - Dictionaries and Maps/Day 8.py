n = int(input())
peoples = {}

for i in range(n):
    names = input().split(" ")
    peoples[names[0]] = names[1]

for k in range(n):
    try:
        s = input()
        if s in peoples:
            print(s+"="+peoples[s])
        else:
            print("Not found")
    except:
        break
    
