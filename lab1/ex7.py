## Write a function that extract a number from a text 

def extract_number(text):
    number = ""
    for char in text:
        if char.isdigit():
            number += char
    return number

print(extract_number("hello world 123"))