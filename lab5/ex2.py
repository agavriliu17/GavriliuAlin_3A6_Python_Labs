#  Create a function and an anonymous function that receive a variable number of arguments. 
#  Both will return the sum of the values of the keyword arguments.

def sum_args_1(*args, **kwargs):
    return sum(kwargs.values())

sum_args_2 = lambda *args,**kwargs: sum(kwargs.values()) 


def main():
    print(sum_args_1(1, 2, c=3, d=4))
    print(sum_args_2(1, b=2, c=3, d=4))

main()