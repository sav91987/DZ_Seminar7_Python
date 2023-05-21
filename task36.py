num_rows = int(input('Введите число строк: '))
num_cols = int(input('Введите число столбцов: '))


def print_operation_table(operation, num_rows, num_cols):
    return operation(num_rows, num_cols)


for i in range(1, num_rows+1):
    for j in range(1, num_cols+1):
        print(print_operation_table(lambda num_rows,
              num_cols: num_cols*num_rows, i, j), end=' ')
    print()
