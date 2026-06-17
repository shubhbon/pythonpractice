#1.Program to create a matrix.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
for row in matrix:
    print(row)


#2.Program to transpose a matrix.

matrix = [
    [1,2,3],
    [4,5,6]
]
rows = len(matrix)
cols = len(matrix[0])

transpose = []

for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)
print("transpose of matrix:")
for row in transpose:
    print(row)



#3.Program to perform the addition and subtraction of two matrices.

A= [
    [1,2,3],
    [4,5,6]
]

B= [
    [7,8,9],
    [1,2,3]
]

rows = len(A)
cols = len(A[0])
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j]+B[i][j])
        result.append(row)

print("Additions of matrices:")
for row in result:
    print(row)


#.4. Program to find matrix inversion.

# Input matrix
a = [[1, 2],
     [3, 4]]

# Calculate determinant
det = a[0][0]*a[1][1] - a[0][1]*a[1][0]

if det == 0:
    print("Inverse does not exist (determinant is 0)")
else:
    inverse = [
        [ a[1][1]/det, -a[0][1]/det],
        [-a[1][0]/det,  a[0][0]/det]
    ]

    print("Inverse of the matrix:")
    for row in inverse:
        print(row)

#5.Program to find a trace of a matrix.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

trace = 0

for i in range(len(matrix)):
    trace += matrix[i][i]

print("Trace of the matrix:", trace)
