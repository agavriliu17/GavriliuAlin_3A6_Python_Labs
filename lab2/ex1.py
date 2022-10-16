# Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main():
    print(fibonacci(10))
   
main()
    

