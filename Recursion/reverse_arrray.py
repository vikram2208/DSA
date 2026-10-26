def reverse_array(my_arr, left, right):
    # Base condition
    if left >= right:
        return my_arr
    my_arr[left], my_arr[right] = my_arr[right], my_arr[left] 

    # Function calling
    return reverse_array(my_arr, left+1, right-1)

print(reverse_array([1,2,3,4,5,6,7,8,9], 3, 6))

# Time complexity is n/2 --> o(n)
# space complexity is N Stack space


# Check if a number is a palindrome

def check_palindrome(my_str, left, right):
    if left >= right:
        return True
    if my_str[left] != my_str[right]:
        print(left , right)
        return False

    return check_palindrome(my_str, left+1, right-1)

print(check_palindrome("malayalam", 0, 8))