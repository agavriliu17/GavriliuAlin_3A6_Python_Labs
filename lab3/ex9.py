# Write a function that receives a variable number of positional arguments and a
# variable number of keyword arguments adn will return the number of positional
# arguments whose values can be found among keyword arguments values.

def count_args(*args, **kwargs):
    count = 0
    for arg in args:
        if arg in kwargs.values():
            count += 1
    return count

def main():
    print(count_args(1, 2, 3, 4, x=1, y=2, z=3, w=5))

main()