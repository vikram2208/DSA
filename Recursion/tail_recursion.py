# Print all numbers from 1 to n using recursion
# Backtracking is also called tail recursion. 

def my_recursion(i,n):
    if i==n:
        return
    my_recursion(i, n-1)
    print(n-1)

my_recursion(1, 5)