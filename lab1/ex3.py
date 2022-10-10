## Write a script that receives two strings and prints the number of occurrences of the first string in the second.

def count_occurrences(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

print(count_occurrences("hello world", "l"))