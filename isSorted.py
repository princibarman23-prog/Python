n=int(input("Enter the number of elements:"))
arr=[]
a=True
for i in range(n):
    x=int(input("Enter elements:"))
    arr.append(x)

for i in range(len(arr)-1):
    if (arr[i]>arr[i+1]):
        a=False

if a:
    print("Yes")
else:
    print("No")