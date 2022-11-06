# Write a function with one parameter which represents a list. The function will return a new list containing all the numbers found in the given list.

def get_numbers(my_list):
    return list(filter(lambda x: type(x) == int or type(x)==float, my_list))

def main():
    print(get_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

main()