def func(a):
    r = 0
    l = 0
    n = len(a)
    j = -1

    for i in range(n):
        l += a[i][i]
        r += a[i][j]
        j -= 1

    return abs(l - r)


a = [
    [1,2,3],
    [4,5,6],
    [9,8,9]
]

result = func(a)
print(result)