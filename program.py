import functions
prompt = 'Please choose the type of matrix operation you would like to compute:' \
         '\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Dot Product\n5. Scalar Multiplication\n6. Transposition\n7. Calculate Determinant\n8. Matrix Inversion'
active = True

while active:
    print(prompt)
    choice = input()

    try:
        choice = int(choice)
    except ValueError:
        print("You must input an integer among the options given.\n")
        continue
    if choice < 1 or choice > 8:
        print("You must input an integer among the options given.\n")
        continue

    if choice > 4:
        count = 1
    else:
        count = 2

    if choice == 5:
        print('Please input the scalar you would like to use to multiply the matrix.')
        scalar = input()
        try:
            scalar = int(scalar)
        except ValueError:
            print('You must input an integer.')
            continue

    matrices = []
    matrix_count = 0
    while matrix_count in range(count):
        print('Please input the number of rows in matrix ' + str(matrix_count + 1) + '.')
        rows = input()
        try:
            rows = int(rows)
        except ValueError:
            print('You must input an integer.')
            continue

        if rows < 1:
            print('The minimum row count is 1.\n')
            continue

        print('Please input the number of columns in matrix ' + str(matrix_count + 1) + '.')
        columns = input()
        try:
            columns = int(columns)
        except ValueError:
            print("You must input an integer.\n")
            continue

        if columns < 1:
            print('The minimum column count is 1.\n')
            continue

        matrix = []
        row_count = 0
        while row_count in range(rows):
            print('Please input row ' + str(row_count + 1) + ' of matrix '
                  + str(matrix_count + 1) + ', formatted as spaced out integers.')
            row = input()
            row = list(row.split(' '))
            if len(row) != columns:
                print('The number of columns in the row do not match the dimensions inputted for this matrix.\n')
                continue

            mistake = False
            for col in range(len(row)):
                try:
                    row[col] = int(row[col])
                except ValueError:
                    print('There is a non-integer entry inputted in the row: ' + row[col] + ".\n")
                    mistake = True
                    break

            if mistake:
                continue

            matrix.append(row)
            row_count += 1

        matrices.append(matrix)
        matrix_count += 1

    if (choice < 3) and (functions.checkSize(matrices[0], matrices[1]) != 1):
        print('These matrices are not the same dimension.\n')
        continue
    if (3 <= choice < 5) and (functions.checkSize(matrices[0], matrices[1]) < 1):
        print('These matrices have incompatible dimensions.\n')
        continue

    if choice == 1:
        result = functions.matrixAdd(matrices[0], matrices[1])
    elif choice == 2:
        result = functions.matrixSub(matrices[0], matrices[1])
    elif choice == 3:
        result = functions.matrixMult(matrices[0], matrices[1])
    elif choice == 4:
        result = functions.matrixDot(matrices[0], matrices[1])
    elif choice == 5:
        result = functions.matrixMultByScalar(matrices[0], scalar)
    elif choice == 6:
        result = functions.matrixTranspose(matrices[0])
    elif choice == 7:
        result = functions.calcDeterminant(matrices[0])
    elif choice == 8:
        result = functions.invertMatrix(matrices[0])

    print('Output:\n')
    for r in range(len(result)):
        print(result[r])
    print('\nWould you like to compute another matrix operation? Press \'Y\' to continue, or any other key to exit.')
    repeat = input()
    if repeat == 'Y':
        continue
    else:
        active = False

