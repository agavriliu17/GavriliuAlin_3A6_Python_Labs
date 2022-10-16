#  Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.

def rhyme(words):
    result = []
    for i in words:
        rhymes_with = [i]
        for j in words:
            if i[-2:] == j[-2:]:
                rhymes_with.append(j)
                words.remove(j)
        result.append(rhymes_with)
    return result

def main():
    print(rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))

main()
