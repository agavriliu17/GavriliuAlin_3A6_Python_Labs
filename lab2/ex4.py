# Write a function that receives as a parameters a list of musical notes (strings), 
# a list of moves (integers) and a start position (integer). The function will return 
# the song composed by going though the musical notes beginning with the start position and 
# following the moves given as parameter.

def compose(notes, moves, start):
    result = []
    for i in moves:
        result.append(notes[start])
        start += i
    return result

def main():
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

main()