def print_formatted(number):
    # your code goes here
    num=len(bin(n)[2:])
    for i in range(1,n+1):
        o=oct(i)[2:]
        h=hex(i)[2:].upper()
        b=bin(i)[2:]
        print (str(i).rjust(num),str(o).rjust(num),str(h).rjust(num),str(b).rjust(num))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
