# Write a function that receives as parameters two lists a and b and returns
# a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)

def get_sets(a, b):
    return [set(a).intersection(b), set(a).union(b), set(a).difference(b), set(b).difference(a)]

def main():
    print(get_sets([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

main()