## Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def convert(string):
    result = ""
    for char in string:
        if char.isupper():
            if result == "":
                result += char.lower()
            else:
                result += "_" + char.lower()
        else:
            result += char
    return result

print(convert("UpperCamelCase"))