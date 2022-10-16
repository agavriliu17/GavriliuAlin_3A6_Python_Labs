# Write a function that will order a list of string tuples based on the 3rd character
# of the 2nd element in the tuple. 
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def sort_tuple(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i][1][2] > list[j][1][2]:
                list[i], list[j] = list[j], list[i]
    return list

def main():
    print(sort_tuple([('abc', 'bcd'), ('abc', 'zza')]))

main()

