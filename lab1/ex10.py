## Write a function that counts how many words exists in a text.

def count_words(text):
    count = 0
    for char in text:
        if char == " ":
            count += 1
    return count + 1

print(count_words("hello world, how are you?"))