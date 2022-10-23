# Write a function that receives a string as a parameter and returns a dictionary 
# in which the keys are the characters in the character string and the values are the 
# number of occurrences of that character in the given text.

def count_letters(text):
    result = {}
    for letter in text:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

def main():
    print(count_letters("Ana has apples"))

main()