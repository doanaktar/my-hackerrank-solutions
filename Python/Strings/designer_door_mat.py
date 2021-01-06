hypen = '-'
welcome = 'WELCOME'
symbol = '.|.'

n, m = map(int,input().split())

i = 0
j = 0
line = int((m-3) / 2)
#top
while i < n//2:
    print(((hypen*line)+(symbol*j)).ljust(int((m-1)/2)-1) +symbol+ ((symbol*j)+(hypen*line)).rjust(int((m-1)/2)-1))
    i+=1
    j+=1
    line-=3

#middle
print(welcome.center(m,hypen))

#bottom
i=0
line+=3 #1 step back because of the while loop on top.
j-=1    #same
while i < n//2:
    print(((hypen*line)+(symbol*j)).ljust(int((m-1)/2)-1) +symbol+ ((symbol*j)+(hypen*line)).rjust(int((m-1)/2)-1))
    i+=1
    j-=1
    line+=3
