# Write a function that receives a list with integers as parameter that contains an equal number of even and odd numbers
# that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers (Xi, Yi)
# such that Xi is the i-th even number in the list and Yi is the i-th odd number

def get_pairs(my_list):
    even = list(filter(lambda x: x % 2 == 0, my_list))
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    return list(zip(even, odd))

def main():
    print(get_pairs([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

main()