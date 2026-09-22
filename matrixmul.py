A=[[0,0],[0,0]]
B=[[0,0],[0,0]]
C=[[0,0],[0,0]]

print("Enter the elements of A:")
for i in range(2):
    for j in range(2):
        A[i][j]=int(input("Enter the elements:"))

print("Enter the elements of B:")
for i in range(2):
    for j in range(2):
        B[i][j]=int(input("Enter the elements:"))

for i in range(2):
    for j in range(2):
        C[i][j]=A=[i][j]*B[i][j]

print("Multiplication of the matrices:")
for i in range(2):
    print(C[i])