import random

list_a = [1,2,3,3,4,5,6,77,7,8,7,8,7,8,7,4,32,1]
list_b = [3,4,7,00,12,45,67,8]

response = {}
for i in list_b:
    for j in list_a:
        if i == j:
            response[i] = response.get(i, 0)+ 1
    if not response.get(i):
        response[i] = 0

print(response)