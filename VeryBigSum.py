def func(a):
    s = 0

    for x in a:
        s += x
    return s

a = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

result = func(a)

print(result)