## Write a functions that determine the most common letter in a string. 

def most_common_letter(string):
    letters = {}
    for char in string:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    max_count = 0
    max_letter = ""
    for letter in letters:
        if letters[letter] > max_count:
            max_count = letters[letter]
            max_letter = letter
    return max_letter

print(most_common_letter("hello world"))