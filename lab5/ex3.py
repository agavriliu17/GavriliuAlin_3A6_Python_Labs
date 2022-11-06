# Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list with all the vowels in a given string.

def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string = 'This is a string with vowels'
    print([x for x in string if x in vowels])
    print(list(filter(lambda x: x in vowels, string)))
    print(list(filter(lambda x: x in vowels, list(string))))

main()