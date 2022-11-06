# Write a function that receives a variable number of arguments and keyword arguments. 
# The function returns a list containing only the arguments which are dictionaries, 
# containing minimum 2 keys and at least one string key with minimum 3 characters.

def get_dicts(*args, **kwargs):
    list1 = list(filter(lambda x: type(x) == dict and len(x) >= 2 and any(type(y) == str and len(y) >= 3 for y in x.keys()), args))
    list2 = list(filter(lambda x: type(x) == dict and len(x) >= 2 and any(type(y) == str and len(y) >= 3 for y in x.keys()), kwargs.values()))

    return list1 + list2

def main():
    print(get_dicts( {1: 2, 3: 4, 5: 6},  {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
                     dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))

main()