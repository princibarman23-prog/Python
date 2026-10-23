n=int(input("Enter  the number of elements:"))
arr=[]
a=True
for i in range(n):
    x=int(input("enter the elements:"))
    arr.append(x)

for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        a=False
        break

if a:
    print("Array is sorted")
else:
    print("Array is not sorted")