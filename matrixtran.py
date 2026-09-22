A=[]
B=[]

print("Ente the elements of matrix A:")
for i in range(2):
    row=[]
    for j in range(2):
        x=int(input("Enter elements:"))
        row.append(x)
    A.append(row)

print("Enter the elements of matrix B:")
for i in range(2):
    row=[]
    for j in range(2):
        x=int(input("Enter elements:"))
        row.append(x)
    B.append(row)

print("Transpose of A:")
for i in range(2):
    for j in range(2):
        print(A[j][i],end=" ")
print()

print("Transpose of B:")
for i in range(2):
    for j in range(2):
        print(B[j][i],end=" ")
print()