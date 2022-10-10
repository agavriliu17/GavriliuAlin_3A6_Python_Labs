## Find The greatest common divisor of multiple numbers read from the console.

def gcd(*numbers):
    def gcd_two(a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a
    result = numbers[0]
    for number in numbers[1:]:
        result = gcd_two(result, number)
    return result

print(gcd(96, 16, 128, 32))

