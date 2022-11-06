# Write a function called process that receives a variable number of keyword arguments
# The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
# If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument 
# and returning True/False) and will retain from the generated numbers only those for which the predicates are True. 
# If the function receives a parameter called limit, it will return only that amount of numbers from the sequence. 
# If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list. 
# The function will return the processed numbers.

def process(**kwargs):
    fib = [0, 1]
    for i in range(2, 1000):
        fib.append(fib[i - 1] + fib[i - 2])

    if 'filters' in kwargs:
        fib = list(filter(lambda x: all(predicate(x) for predicate in kwargs['filters']), fib))

    if 'offset' in kwargs:
        fib = fib[kwargs['offset']:]

    if 'limit' in kwargs:
        fib = fib[:kwargs['limit']]

    return fib

def sum_digits(x):
    return sum(map(int, str(x)))

def main():
    x = process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2)
    print(x)

main()