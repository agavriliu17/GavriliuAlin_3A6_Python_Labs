# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def prime_numbers(numbers):
    prime = []
    for num in numbers:
        if num > 1:
            for i in range(2, int(num/2)):
                if (num % i) == 0:
                    break
            else:
                prime.append(num)
    return prime

def main():
    print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

main()