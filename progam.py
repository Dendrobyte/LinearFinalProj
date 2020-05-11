import functions
prompt = 'Please choose the type of matrix operation you would like to compute:' \
         '\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Dot Product\n5. Transposition'
active = True

while active:
    print(prompt)
    choice = input()

    try:
        choice = int(choice)
    except ValueError:
        print("You must input an integer among the options given.")
        continue
    if choice < 1 or choice > 5:
        print("You must input an integer among the options given.")
        continue

    if choice != 4 and choice != 5:
        print('How many matrices are there?')
        count = input()
    else:
        count = 1

    try:
        count = int(count)
    except ValueError:
        print("You must input an integer.")
        continue

    if (choice != 4 and choice != 5) and count < 2:
        print('This operation requires at least two matrices to be inputted.')
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
            print('The minimum row count is 1')
            continue

        print('Please input the number of columns in matrix ' + str(matrix_count + 1) + '.')
        columns = input()
        try:
            columns = int(columns)
        except ValueError:
            print("You must input an integer.")
            continue

        if columns < 1:
            print('The minimum column count is 1')
            continue

        matrix = []
        row_count = 0
        while row_count in range(rows):
            print('Please input row ' + str(row_count + 1) + ' of matrix '
                  + str(matrix_count + 1) + ', formatted as spaced out integers.')
            row = input()
            row = list(row.split(' '))
            if len(row) != columns:
                print('The number of columns in the row do not match the dimensions inputted for this matrix.')
                continue

            mistake = False
            for col in range(len(row)):
                try:
                    row[col] = int(row[col])
                except ValueError:
                    print('There is a non-integer entry inputted in the row: ' + row[col] + ".")
                    mistake = True
                    break

            if mistake:
                continue

            matrix.append(row)
            row_count += 1

        matrices.append(matrix)
        matrix_count += 1

    print(matrices)

