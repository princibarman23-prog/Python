n=int(input("Enter number of elements:"))
a=[];
for i in range(n):
    x=int(input("Enter the elements"))
    a.append(x)
key=int(input("Enter element to search:"))
found=False
for i in range(n):
    if a[i]==key:
        print("Element found at index:",i)
        found=True
        break
if found==False:
    print("Element not found")