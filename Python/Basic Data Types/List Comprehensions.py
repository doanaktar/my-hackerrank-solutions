if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = []
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if (a + b + c) != n:
                    result.append([a, b, c])
    
    print(result)

    '''
    This solutin looks better than mine
    x, y, z, n = (int(input()) for _ in range(4))
    print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)
    if a + b + c != n ])    
    '''
