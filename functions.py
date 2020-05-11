# Functions.py to be used in the program.py main file.
# Test cases can be found on the jupyter notebook.
# Starts with basic functions, then matrix inversion, then LU factorization

'''
Check size

mat1, mat2 - 2D lists (matrices) to check whether they are the same dimensions
RETURNS resultInt - 0 if they share nothing, 1 if they are the same dimensions, 2 if they share the "middle" dimension,
i.e. M(p,q) and N(i,j) would return 2 if q == i
'''
def checkSize(mat1, mat2):
    mat1_dim1 = len(mat1) # p
    mat1_dim2 = len(mat1[0]) # q
    mat2_dim1 = len(mat2) # i
    mat2_dim2 = len(mat2[0]) # j
    if(mat1_dim1 != mat2_dim1):
        if(mat1_dim2 == mat2_dim1):
            return 2 # q and i match
        else:
            return 0 # dimensions are not the same anywhere
    elif(mat1_dim1 == mat2_dim1):
        if(mat1_dim2 == mat2_dim2):
            return 1 # dimensions are the exact same
        elif(mat1_dim2 == mat2_dim1):
            return 2 # still check for this a second time
        else:
            return 0 # first dimensions match, but the second two don't
    
'''
Matrix Addition

mat1, mat2 - 2D lists (matrices) to be added
RETURNS resultMat - The resulting matrix from the addition of mat1 and mat2, empty list if mat1 and mat2 are invalid
'''
def matrixAdd(mat1, mat2):
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
    resultMatrix = []*dim2
    if(checkSize(mat1, mat2) != 1):
        print("Matrices can not be added. Dimension mismatch.")
        resultMatrix = []
    else:
        for i in range(dim1):
            newRow = [0]*dim1 # Need this notation since attempting a double multiplication leads to reference variable issues
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
    mat1_dim1 = len(mat1) # q
    mat1_dim2 = len(mat1[0]) # p
    mat2_dim1 = len(mat2) # j
    mat2_dim2 = len(mat2[0]) # i
    resultMatrix = []*mat1_dim1
    if(checkSize(mat1, mat2) == 0):
        print("Matrices can not be dotted. Dimension mismatch.")
        resultMatrix = []
    else:
        for p in range(mat1_dim2):
            newRow = []
            for j in range(mat2_dim2):
                newIndex = 0
                for q in range(mat1_dim1): #recall q = i
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