def isPalindrome(x: int) -> bool:

    if x < 0:
        return False

    list_x = [int(i) for i in str(x)]
    reversed_x = list_x[::-1]
    if (list_x == reversed_x):
        return True
    else:
        return False


x = 121
print(isPalindrome(x))
