# Write a function that receives as parameter a matrix which represents the 
# heights of the spectators in a stadium and will return a list of tuples (line, column) 
# each one representing a seat of a spectator which can't see the game. 
# A spectator can't see the game if there is at least one taller spectator standing in front of him. 
# All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, 
# beginning with the closest row from the field.

def obstructed(matrix):
    result = []

    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])):
            if matrix[i][j] > matrix[i+1][j]:
                result.append((i+1, j))
    return result

def main():
    print(obstructed([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))

main()
