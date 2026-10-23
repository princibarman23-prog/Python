A=[[0,0],[0,0]]
B=[[0,0],[0,0]]

print("Enter the elements of matrix A:")
for i in range(2):
    for j in range(2):
        A[i][j]=int(input("Enter elements:"))

print("Enter the elements of matrix B:")
for i in range(2):
    for j in range(2):
        B[i][j]=int(input("Enter elements:"))

for i in range(2):
    for j in range(2):
        B[i][j]=A[i][j]

print("Matrix Transpose:")
for i in range(2):
    print(B[i])