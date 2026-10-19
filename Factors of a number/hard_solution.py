from math import sqrt
def get_factorial(my_num):
    response = []
    my_num_sqrt = int(sqrt(my_num))
    for i in range(1, my_num_sqrt):
        if my_num % i == 0:
            response.append(i)
            if my_num != i:
                response.append(my_num//i)
    return response

print(get_factorial(38))