# Write a function that, for a text given as a parameter, censures words that begin and end with vowels. 
# Censorship means replacing characters from odd positions with *.

import re

def censor_words(text):
    words = []
    word = ''
    for i in text:
        if i.isalnum():
            word += i
        else:
            if word != '':
                words.append(word)
            word = ''
    if word != '':
        words.append(word)

    censored_words = []
    for i in words:
        if re.match('[aeiou]', i[0]) and re.match('[aeiou]', i[-1]):
            censored_word = ''
            for j in range(len(i)):
                if j % 2 == 0:
                    censored_word += i[j]
                else:
                    censored_word += '*'
        
        censored_words.append(censored_word)
    return censored_words

def main():
    text = input('Enter text: ')
    words = censor_words(text)
    print(words)

main()
