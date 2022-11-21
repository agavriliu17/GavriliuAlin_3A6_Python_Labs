# Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters.

def extract_words(text):
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
    return words



def main():
    text = input('Enter text: ')
    words = extract_words(text)
    print(words)

if __name__ == '__main__':
    main()
