def compareTriplets(a, b):
    result = [0, 0]
    n = len(a)
    for i in range(n):
        if a[i] > b[i]:
            result[0] += 1
        elif a[i] < b[i]:
            result[1] += 1
            
    return result

a = [1, 2, 3]
b = [3, 2, 1]

result = compareTriplets(a, b)

print(result)