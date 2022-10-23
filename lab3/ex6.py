# Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list, and b representing the 
# number of duplicate elements in the list (use sets to achieve this objective).

def count_unique_duplicate(lst):
    unique = set(lst)
    return len(unique), len(lst) - len(unique)

def main():
    print(count_unique_duplicate([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

main()