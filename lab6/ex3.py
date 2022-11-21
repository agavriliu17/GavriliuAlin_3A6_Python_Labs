# Write a function that receives as a parameter a string of text characters and a list of regular expressions 
# and returns a list of strings that match on at least one regular expression given as a parameter.

import re
from ex1 import extract_words

def match_expressions(text, regex_list):
    words = extract_words(text)
    matches = []

    for word in words:
        for regex in regex_list:
            if re.match(regex, word):
                matches.append(word)
                break
    return matches

def main():
    words = match_expressions("I have to pay 300$", [r'[aeiou]', r'[0-9]'])
    print(words)

main()