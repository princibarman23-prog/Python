n=int(input("Enter number of elements:"))
a=[]
for i in range(n):
    x=int(input("Enter element:"))
    a.append(x)
a.sort()
print("Sorted list:",a)

key=int(input("Enter element"))