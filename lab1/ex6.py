## Write a function that validates if a number is a palindrome.

def is_palindrome(number):
    string = str(number)
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            return False
    return True


print(is_palindrome(12321))
print(is_palindrome(12345))