
def get_factors(my_num):
    result = []
    for i in range(1, my_num//2):
        if my_num%i==0:
            result.append(i)
    return result

print(get_factors(37))