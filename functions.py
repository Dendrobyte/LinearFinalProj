# All matrices will be in the format of 2D lists

'''
Check size

mat1, mat2 - 2D lists (matrices) to check whether they are the same dimensions
RETURNS resultInt - 0 if they share nothing, 1 if they are the same dimensions, 2 if they share the "middle" dimension,
i.e. M(p,q) and N(i,j) would return 2 if q == i
'''


def checkSize(mat1, mat2):
    mat1_dim1 = len(mat1)  # p
    mat1_dim2 = len(mat1[0])  # q
    mat2_dim1 = len(mat2)  # i
    mat2_dim2 = len(mat2[0])  # j
    if (mat1_dim1 != mat2_dim1):
        if (mat1_dim2 == mat2_dim1):
            return 2  # q and i match
        else:
            return 0  # dimensions are not the same anywhere
    elif (mat1_dim1 == mat2_dim1):
        if (mat1_dim2 == mat2_dim2):
            return 1  # dimensions are the exact same
        elif (mat1_dim2 == mat2_dim1):
            return 2  # still check for this a second time
        else:
            return 0  # first dimensions match, but the second two don't


'''
Matrix Addition

mat1, mat2 - 2D lists (matrices) to be added
RETURNS resultMat - The resulting matrix from the addition of mat1 and mat2, empty list if mat1 and mat2 are invalid
'''


def matrixAdd(mat1, mat2):
    # Initialize starting matrix
    dim1 = len(mat1)
    dim2 = len(mat1[0])
    resultMatrix = [] * dim2
    if (checkSize(mat1, mat2) != 1):
        print("Matrices can not be added. Dimension mismatch.")
        resultMatrix = []
    else:
        for i in range(dim1):
            newRow = [
                         0] * dim1  # Need this notation since attempting a double multiplication leads to reference variable issues
            for j in range(dim2):
                newRow[j] = mat1[i][j] + mat2[i][j]
            resultMatrix.append(newRow)

    return resultMatrix


'''
Matrix Subtraction

mat1, mat2 - 2D Lists (matrices) to be subtracted
RETURNS resultMat - The resulting matrix from the subtraction of mat1 and mat2, empty list if mat1 and mat2 are invalid
'''


def matrixSub(mat1, mat2):
    # Initialize starting matrix
    dim1 = len(mat1)
    dim2 = len(mat1[0])
    resultMatrix = [] * dim2
    if (checkSize(mat1, mat2) != 1):
        print("Matrices can not be added. Dimension mismatch.")
        resultMatrix = []
    else:
        for i in range(dim1):
            newRow = [
                         0] * dim1  # Need this notation since attempting a double multiplication leads to reference variable issues
            for j in range(dim2):
                newRow[j] = mat1[i][j] - mat2[i][j]
            resultMatrix.append(newRow)

    return resultMatrix


'''
Matrix Multiplication

mat1, mat2 - 2D Lists (matrices) to be multiplied. This is NOT the dot product.
RETURNS resultMat - The resulting matrix from the multiplication of mat1 and mat2, empty list if mat1 and mat2 are invalid
'''


def matrixMult(mat1, mat2):
    return matrixDot(mat1, mat2) # I don't think matrix multiplication is a thing, oops
    # Initialize starting matrix
    dim1 = len(mat1)
    dim2 = len(mat1[0])
    resultMatrix = []*dim2
    if(checkSize(mat1, mat2) != 1):
        print("Matrices can not be added. Dimension mismatch.")
        resultMatrix = []
    else:
        for i in range(dim1):
            newRow = [0]*dim1 # Need this notation since attempting a double multiplication leads to reference variable issues
            for j in range(dim2):
                newRow[j] = mat1[i][j] * mat2[i][j]
            resultMatrix.append(newRow)
        
    return resultMatrix


'''
Matrix Multiplication by a Scalar

mat - Matrix involved in the operation
scal - The scalar the matrix is being multiplied by
RETURNS resultMat - The matrix with each index multiplied by scal. Returns new matrix so the input matrix is untouched.
'''


def matrixMultByScalar(mat, scal):
    # Create deep copy so we avoid editing the given matrix (could have also created new array like earlier)
    import copy
    newMat = copy.deepcopy(mat)

    # Multiply each element by the given scalar
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            newMat[i][j] = scal * mat[i][j]

    return newMat


'''
Matrix Dot Product

mat1, mat2 - 2D Lists (matrices) to be dotted.
RETURNS resultMat - The resulting matrix from the dot product of mat1 and mat2, empty list if mat1 and mat2 are invalid
'''


def matrixDot(mat1, mat2):
    # The dimensions(dim1 and dim2) should be named the other way around... apologies :(
    mat1_dim1 = len(mat1)  # q
    mat1_dim2 = len(mat1[0])  # p
    mat2_dim1 = len(mat2)  # j
    mat2_dim2 = len(mat2[0])  # i
    resultMatrix = [] * mat1_dim1
    if (checkSize(mat1, mat2) == 0):
        print("Matrices can not be dotted. Dimension mismatch.")
        resultMatrix = []
    else:
        for p in range(mat1_dim2):
            newRow = []
            for j in range(mat2_dim2):
                newIndex = 0
                for q in range(mat1_dim1):  # recall q = i
                    newIndex += mat1[p][q] * mat2[q][j]
                newRow.append(newIndex)
            resultMatrix.append(newRow)
    return resultMatrix


'''
Matrix Transpose
mat - 2D List (matrix) to be transposed
RETURNS resultMat - The transposed matrix. Returns new matrix so the input matrix is untouched.
'''


def matrixTranspose(mat):
    # Create deep copy so we avoid editing the given matrix (could have also created new array like earlier)
    import copy
    newMat = copy.deepcopy(mat)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            newMat[i][j] = mat[j][i]
    return newMat
    
# Determinant Calculator
'''
Calculate Determinant
mat - Matrix to find the determinant of

RETURNS det - The determinant of the matrix
'''

def calcDeterminant(mat):
    det = 0
    # Trick from the previous site
    dim1 = len(mat)
    dim2 = len(mat[0])
    indices = list(range(dim1))
     
    # 2x2 matrix base case since I'm doing this recursively
    if dim1 == 2 and dim2 == 2:
        baseDet = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return baseDet
 
    for col in indices:
        # Create a submatrix
        import copy
        modMat = copy.deepcopy(mat)
        modMat = modMat[1:]
        numRows = len(modMat)
 
        for row in range(numRows): 
            modMat[row] = modMat[row][0:col] + modMat[row][col+1:]
        
        # Get the sign of the current column
        sign = (-1) ** (col % 2)
        # Find determinant of our "submatrix"
        subMatDet = calcDeterminant(modMat)
        # Add up all sub determinants to get final determinant
        det += sign * mat[0][col] * subMatDet
 
    return det
    
# Matrix Inversion

'''
Ensure Square Matrix
mat - 2D List (matrix) to be checked

RETURNS square - True if square matrix, false if non-square matrix
'''
def ensureSquareMatrix(mat):
    dim1 = len(mat)
    dim2 = len(mat[0])
    if(dim1 == dim2): return True
    else: return False

'''
Create Identity Matrix
dim - Integer representing the dimension of the matrix to be generated

RETURNS identityMat - Identify matrix of dimension dim
'''
def createIdentityMatrix(dim):
    identityMat = []
    for i in range(dim):
        newRow = [0]*dim
        for j in range(dim):
            if(i == j):
                newRow[i] = 1
        identityMat.append(newRow)
    return identityMat

'''
Invert Matrix
mat - 2D List (matrix) to be inverted

RETURNS invertedMat - Inverted version of the given matrix, leaving original matrix unedited
STATUS: Currently very dysfunctional :,(
'''


def invertMatrix(mat):
    if (ensureSquareMatrix(mat) == False):
        print("Matrix can not be inverted - Matrix not square.")
        return mat

    import copy
    dim = len(mat)
    invertedMat = copy.deepcopy(mat)  # Deep copy to leave the original
    identityMat = createIdentityMatrix(dim)

    # We now proceed with our row operations
    indices = list(range(dim))
    for diagonal in range(dim):
        diagInt = 1.0 / invertedMat[diagonal][diagonal]
        for col in range(dim):  # Tackle columns
            invertedMat[diagonal][col] *= diagInt
            identityMat[diagonal][col] *= diagInt
        'This is where the website in the cell above comes in. Avoiding the diagonals was just a matter of slicing.'
        for row in indices[0:diagonal] + indices[diagonal + 1:]:  # Tackle rows -- The slicing skips the diagonal
            rowInt = invertedMat[row][diagonal]
            for el in range(dim):
                invertedMat[row][el] = invertedMat[row][el] - rowInt * invertedMat[diagonal][el]
                identityMat[row][el] = identityMat[row][el] - rowInt * identityMat[diagonal][el]
    return invertedMat