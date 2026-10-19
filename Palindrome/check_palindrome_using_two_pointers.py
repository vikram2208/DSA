name = "madam"

def check_palindrome(text_var):
    left = 0
    right = len(text_var) - 1

    while left < right:
        if text_var[left] != text_var[right]:
            return False
        left += 1
        right -= 1

    return True

print(check_palindrome(name))