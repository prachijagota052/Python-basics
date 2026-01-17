def multiply_matrices(a,b):
    result=0
    rows_a=len(a)
    rows_b=len(b)
    cols_a=len(a[0])
    cols_b=len(b[0])
    if rows_a!=cols_b:
        print("incompatible")
    else:
        for i in rows_a:
            for j in cols_b:
                for k in cols_a:
                    result[i][j] += a[i][k] * b[k][j]
                    print(result)
a=input("enter matrix1")
b=input("enter matrix2")
print(multiply_matrices(a,b))