#  Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs).
#  The function should return a list of dictionaries for each pair (in the same order as in the input list)
#  that contain the following keys (as strings): 
#  sum (the value should be sum of the 2 numbers),
#  prod (the value should be product of the two numbers),
#  pow (the value should be the first number raised to the power of the second number) 

def calcs(pairs):
    return list(map(lambda x: {'sum': x[0] + x[1], 'prod': x[0] * x[1], 'pow': x[0] ** x[1]}, pairs))

def main():
    print(calcs([(5, 2), (19, 1), (30, 6), (2, 2)]))

main()
