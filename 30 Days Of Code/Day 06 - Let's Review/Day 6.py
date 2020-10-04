# Enter your code here. Read input from STDIN. Print output to STDOUT
count = int(input())
words = []
even = ""
odd = ""

for _ in range(count):
    words_item = input().strip()
    for i in range(len(words_item)):
        if i % 2 == 0:
            even += words_item[i]
        else:
            odd += words_item[i]
    print(even + " " + odd)
    even = ""
    odd = ""
