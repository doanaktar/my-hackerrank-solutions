n = int(input().strip())
if (
n % 2 == 0 and(
n in range(2,6) or
n > 20
)):
   print("Not Weird")
else:
    print("Weird")
