# Functional recursion
# formula = n * f(n-1)

def factorial(start, end, total):
    if start==end:
        return total
    
    return start * factorial(start + 1, end, total)

print(factorial(1,11,1))