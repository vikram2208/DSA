list_a = [1,2,3,3,4,5,6,7,7,8,7,8,7,8,7,4,3,1]
list_b = [3,4,7,00,12,45,67,8]

hash_list = [0] * 11

# 1. With hash  (space complexity is m+n)
# 2. With dictonary 

for i in list_a:
    hash_list[i] = hash_list[i] + 1
for j in list_b:
    if 0 < j and 10 > j:
        print(f"{j} is {hash_list[j]} times")

# Using dictonary
response = {}
list_a = [1,2,3,3,4,5,6,7,7,8,7,8,7,8,7,4,3,1]
list_b = [3,4,7,00,12,45,67,8]

for i in list_a:
    response[i] = response.get(i, 0) + 1

for j in list_b:
    print(f"Element {j} is {response.get(j, 0)} times")