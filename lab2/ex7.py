# Write a function that receives as parameter a list of numbers (integers) and will 
# return a tuple with 2 elements. The first element of the tuple will be the number of 
# palindrome numbers found in the list and the second element will be the greatest palindrome number.

def palindrome(numbers):
    palindrome = []
    for num in numbers:
        if num == int(str(num)[::-1]):
            palindrome.append(num)
    return (len(palindrome), max(palindrome))

def main():
    print(palindrome([100, 101, 10, 11, 121, 131, 141, 151]))

main()