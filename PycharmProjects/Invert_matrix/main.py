

def print_matrix(M1,M2 = []):
    m_rows = len(M1)
    m_cols = len(M1[0])
    for i in range(m_rows):
        if M2 != []:
            print(M1[i],'|',M2[i])
        else:
            print(M1[i])

def add_rows(M,M2=[]):
    r1 = int(input("Which row you want to change? (enter e to exit) ")) - 1
    c1 = float(input("Coefficient for the row to change?"))
    r2 = int(input("Which row you want to add?")) - 1
    c2 = float(input("Coefficient for the row to add?"))
    for i in range(len(M[0])):
        a = M[r1][i]*c1
        b = M[r2][i]*c2
        M[r1][i] = a + b
    if M2 != []:
        for i in range(len(M2[0])):
            a = M2[r1][i] * c1
            b = M2[r2][i] * c2
            M2[r1][i] = a + b

def s_rows(M,r1,r2):
    M.insert(r2, M[r1])
    M.insert(r1, M[r2 + 1])
    M.pop(r1 + 1)
    M.pop(r2 + 1)
    return M

def swap_rows(M, M2 = []):
    r1 = int(input("Enter the first row number ")) - 1
    r2 = int(input("Enter the second row number ")) - 1
    if r1 > r2:
        r = r1
        r1 = r2
        r2 = r
    M = s_rows(M,r1,r2)
    if M2 != []:
        M2 = s_rows(M2, r1, r2)


def normalize_matrix(M1,M2):      # normalazing M2 when M1 is already diagonal matrix

    for i in range(3):
        coeff = M1[i][i]
        M1[i][i] = M1[i][i] /coeff
        for j in range(3):
            M2[i][j] = M2[i][j] /coeff


def invert_matrix(M1):
    M0 = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
    M2 = M0
    while True:
        print_matrix(M1,M2)
        op = input("a to add two rows, s to swap rows, e to exit\n>>>>")
        if op == 'e':
             normalize_matrix(M1,M2)
             break
        elif op == 'a':
            add_rows(M1,M2)
        elif op == 's':
            swap_rows(M1,M2)

    return M2

def row_reduction(M1):
    while True:
        print_matrix(M1)
        operation = input("a to add two rows, s to swap rows, e to exit\n>>>>")
        if operation == 'a':
            add_rows(M1)
        elif operation == 's':
            swap_rows(M1)
        elif operation == 'e':
            break

    return M1

def main():
    if input("Invert matrix (Linear Algebra Q4c)? y/n") == 'y':
        M = [[-1,1,0],[1,2,1],[-1,-2,1]]
        MI = invert_matrix(M)
        print("Inverted matrix",MI)
    if input("Row reduction (Linear Algebra Q2)? y/n") == 'y':
        M = [[2,-1, 1, 2], [1, 2, 1,3], [5, -5, 2,3]]
        MR = row_reduction(M)
        print("Row reduced matrix")
        print_matrix(M)

main()