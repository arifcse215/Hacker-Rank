def extraLongFactorials(n):
    if n == 1:
        return 1
    else:
        return n*extraLongFactorials(n-1)

n = int(input())
r = extraLongFactorials(n)
print(r)