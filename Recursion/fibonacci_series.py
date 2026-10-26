def my_fibbo(n):
    if n == 1:
        return 1
    return n + my_fibbo(n - 1)

print(my_fibbo(9))

def my_fibbo2(n):
    if n == 1:
        return 1
    return my_fibbo2(n + (n - 1))