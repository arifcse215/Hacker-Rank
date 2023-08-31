number_of_size = int(input())
size_list = list(map(int, input().split(" ")))
total_customer = int(input())

total_sale = 0

for x in range(total_customer):
    p, q = map(int, input().split(" "))
    if p in size_list:
        total_sale += q
        size_list.remove(p)
        
print(total_sale)
