from sympy import N


def plusMinus(arr):
    p = 0
    m = 0
    for x in arr:
        if x > 0:
            p += 1
        elif x < 0:
            m += 1

    n = len(arr)
    z = n - (p + m)

    print(p/n)
    print(m/n)
    print(z/n)

arr = [1,1,0,-1,-1]

result = plusMinus(arr)
