from collections import Counter
no_of_lines = int(input())
all_shoes = Counter(map(int, input().split()))
total_money_earned = 0
for cust in range(int(input())):
    data = input().split()
    shoe_size = int(data[0])
    price = int(data[1])
    if shoe_size in all_shoes.keys() and all_shoes[shoe_size] > 0:
        total_money_earned += price
        all_shoes[shoe_size] -= 1

print(total_money_earned)