def f1(a,n,m):
    col = 1
    for i in range(0,n):
        for j in range(0,col):
            if(a[i][j] != 0):
                return False
        col += 1

    return True

def f2(a,n,m):
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0
    while(i<n and j<m):
        sum1 += a[i][j]
        sum2 += a[i][m-j-1]
        i+=1
        j+=1

    daigonal = [sum1,sum2]
    return daigonal


def f3(a,n,m):
    col = 0
    for i in range(0,n):
        for j in range(0,col):
            temp = a[i][j]
            a[i][j] = temp
            a[j][i] = temp
        col += 1

    return a

def add(a,b,n,m):
    for i in range(0,n):
        for j in range(0,m):
            a[i][j] += b[i][j]
    return a

def sub(a,b,n,m):
    for i in range(0,n):
        for j in range(0,m):
            a[i][j] -= b[i][j]
    return a

def mul(a,b,n1,m1,n2,m2):
    final = []
    for row in range (0,n1):
        #rows
        li = []
        for col in range (0,m1):
            i = 0
            sum = 0
            while(i<m1):
                sum += a[row][i]*b[i][col]
                #print(row," ",i," ",col)
                i+=1
            li.append(sum)
        final.append(li)

    return final

def f5(a,n,m):
    for i in range(0,n):
        for j in range(0,m):
            #ele = a[i][j]
            flag = True
            for k in range(0,n):
                #traveling in row 
                if(a[k][j] >= a[i][j]):
                    return False
                
            for k in range(0,m):
                if(a[i][k] >= a[i][j]):
                    return False
            if(flag == True):
                ans = [i,j]
                return ans
            
    return -1

def createMatrix(n,m):
    matrix = []
    for row in range(0,n):
        li = []
        for col in range(0,m):
            li.append(int(input()))
        matrix.append(li)

    return matrix


def magicalSquare(matrixA,n,m):
    daigonalsum = f2(matrixA,n,m)
    if(daigonalsum[0] == daigonalsum[1]):
        for row in range(0,n):
            p = 0
            sum = 0
            for p in range(0,m):
                sum += matrixA[row][p]
            if(sum != daigonalsum[0]):
                return False
        
        for col in range(0,m):
            p = 0
            sum = 0
            for p in range(0,n):
                sum += matrixA[p][col]
            if(sum != daigonalsum[0]):
                return False
        
        return True
    
    else:
        return False



print("Enter your choice: ")
print("1. Check whether a given matrix is upper traingular or not.")
print("2. Compute summution of diagonal element.")
print("3.Compute transpose of matrix ")
print("4. Add 2 matrix ")
print("5. Subtract 2 matrix ")
print("6. multiply 2 Matrix")
print("7. Find Saddle point in matrix")
print("8. To check for magical matrix ")
print()
choice = int(input("Enter choice: "))

if(choice == 1):
    n = int(input("Enter no. of rows: "))
    m = int(input("Enter no. of col: "))
    matrixA = createMatrix(n,m)
    if(f1(matrixA,n,m) == True):
        print("Given Matrix is upper trangular ")
    else:
        print("Given Matrix is not upper trangular ")
    

elif(choice == 2):
    n = int(input("Enter no. of rows: "))
    m = int(input("Enter no. of col: "))
    matrixA = createMatrix(n,m)
    print(f2(matrixA,n,m))

elif(choice == 3):
    n = int(input("Enter no. of rows: "))
    m = int(input("Enter no. of col: "))
    matrixA = createMatrix(n,m)
    print(f3(matrixA,n,m))

elif(choice == 4):
    n1 = int(input("Enter no. of rows: "))
    m1 = int(input("Enter no. of col: "))
    matrixA = createMatrix(n1,m1)
    n2 = int(input("Enter no. of rows: "))
    m2 = int(input("Enter no. of col: "))
    matrixB = createMatrix(n2,m2)
    print(add(matrixA,matrixB,n1,m1))

elif(choice == 5):
    n1 = int(input("Enter no. of rows: "))
    m1 = int(input("Enter no. of col: "))
    matrixA = createMatrix(n1,m1)
    n2 = int(input("Enter no. of rows: "))
    m2 = int(input("Enter no. of col: "))
    matrixB = createMatrix(n2,m2)
    print(sub(matrixA,matrixB,n1,m1))

elif(choice == 6):
    n1 = int(input("Enter no. of rows: "))
    m1 = int(input("Enter no. of col: "))
    matrixA = createMatrix(n1,m1)
    n2 = int(input("Enter no. of rows: "))
    m2 = int(input("Enter no. of col: "))
    matrixB = createMatrix(n2,m2)
    print(mul(matrixA,matrixB,n1,m1,n2,m2))

elif(choice == 7):
    n1 = int(input("Enter no. of rows: "))
    m1 = int(input("Enter no. of col: "))
    matrixA = createMatrix(n1,m1)
    print(f5(matrixA,n1,m1))

elif(choice == 8):
    n1 = int(input("Enter no. of rows: "))
    m1 = int(input("Enter no. of col: "))
    matrixA = createMatrix(n1,m1)

    if(magicalSquare(matrixA,n1,m1) == True):
        print("Given Matrix is a Magical Matrix .")
    
    else:
        print("Given Matrix is not a magical matrix")
    
       
else:
    print("Wrong choice .")



