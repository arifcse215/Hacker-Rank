def staircase(n):
    a = '#'
    s = ' '

    for x in range(n):
        for y in range(n-x-1):
            print(s, end='')
        for z in range(x+1):
            print(a, end='')
        print()

staircase(int(input()))