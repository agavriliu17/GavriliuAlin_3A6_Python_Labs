# Write a function that receives a number x, default value equal to 1, a list of strings, 
# and a boolean flag set to True. For each string, generate a list containing the characters 
# that have the ASCII code divisible by x if the flag is set to True, otherwise it should contain 
# characters that have the ASCII code not divisible by x.

def ascii_divisible(strings, x=1, flag=True):
    result = []
    for string in strings:
        temp = []
        for char in string:
            if flag and ord(char) % x == 0:
                temp.append(char)
            elif not flag and ord(char) % x != 0:
                temp.append(char)
        result.append(temp)
    return result

def main():
    print(ascii_divisible(["test", "hello", "lab002"], 2, flag=False))

main()