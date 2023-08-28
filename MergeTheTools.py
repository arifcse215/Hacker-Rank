def merge_the_tools(string, k):
    # your code goes here
    x = 0
    y = k
    u = []
    t = []
    a = len(string)
    a = int(a/k)
    for i in range(a):
        for j in range(x, y):
            t.append(string[j])
          
        x = y
        y += k
        
        for p in t:
            if p not in u:
                u.append(p)
                

        for q in u:
            print(q, end="")
        print()
            
        u.clear()
        t.clear()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
