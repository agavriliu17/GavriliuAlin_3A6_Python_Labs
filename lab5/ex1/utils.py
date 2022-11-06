# Write a module named utils.py that contains one function called process_item. 
# The function will have one parameter, x, and will return the least prime number greater than x. 
# When run, the module will request an input from the user, convert it to a number and it will display the output of the process_item function.

def process_item(x):
    if x <= 1:
        return 2
    for i in range(x + 1, 2 * x):
        if all(i % j != 0 for j in range(2, i)):
            return i

def main():
    x = int(input("Enter a number: "))
    print(process_item(x))
    