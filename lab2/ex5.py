# Write a function that receives as parameter a matrix and will return the matrix obtained by 
# replacing all the elements under the main diagonal with 0 (zero).
def zero_under_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix

def main():
    print(zero_under_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

main()