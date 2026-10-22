# Print all numbers from 1 to n using recursion


def my_recursion(i,n):
    if i==n:
        return
    print(i)
    my_recursion(i+1, n)

my_recursion(1, 5)