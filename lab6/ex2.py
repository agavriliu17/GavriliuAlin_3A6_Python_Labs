# Write a function that receives as a parameter a regex string, a text string and a whole number x, 
# and returns those long-length x substrings that match the regular expression.

import re
from ex1 import extract_words

def match_words(regex, text, x):
    words = extract_words(text)
    matches = []
    for word in words:
        if re.match(regex, word) and len(word) == x:
            matches.append(word)
    return matches


def main():
    words = match_words(r'[aeiou]', 'This is a test', 2)
    print(words)

main()
    