# Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def intersect(a, b):
    return list(set(a) & set(b))

def union(a, b):
    return list(set(a) | set(b))

def difference(a, b):
    return list(set(a) - set(b))

def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(intersect(a, b))
    print(union(a, b))
    print(difference(a, b))

main()