# Find factorial using parameterized recusion

# pattern = f(n-1, result * n)

# Find factorial using paramterized recusrion

def factorial(start, end, total):
    if start == end:
        return total

    return factorial(start+1, end, start*total)

print(factorial(1,11,1))