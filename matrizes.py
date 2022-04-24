
def shape(a):
    num_rows = len(a)
    num_columns = len(a[0]) if a else 0
    return num_rows, num_columns

def get_row(a, i):
    return a[i]

def get_column(a, j):
    return [a_i[j] for a_i in a]

matriz_ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(shape(matriz_ex))
print(get_row(matriz_ex, 1))
print(get_column(matriz_ex, 1))

def make_matrizes(num_rows, num_cols, entry_fn):
    return [
        [entry_fn(i, j) for j in range(num_cols)] 
        for i in range (num_rows)
    ]
