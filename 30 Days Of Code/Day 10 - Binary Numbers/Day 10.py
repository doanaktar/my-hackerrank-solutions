if __name__ == '__main__':
    n = int(input())
    a = bin(n)[2:].split('0')
    print(len(max(a)))
