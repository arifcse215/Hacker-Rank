def pangrams(s):
    c = [chr(i) for i in range(97, 123)]

    for x in s:
        if len(c) != 0 and x.lower() in c:
            c.remove(x.lower())
        if len(c) == 0:
            return 'pangram'

    if len(c) != 0:
        return 'not pangram'
s = input()

result = pangrams(s)

print(result)
