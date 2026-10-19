elem1 = "Sathish"

to_check_elem = ""
check_elem = elem1
while check_elem:
    to_check_elem = to_check_elem + check_elem[-1]
    check_elem = check_elem[:-1]

if elem1 == to_check_elem:
    print("This is a palindrome")
else:
    print(elem1, to_check_elem)
    print("Not a palindrome")
