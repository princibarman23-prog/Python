n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    x=int(input("Enter elements:"))
    arr.append(x)

max=arr[0]
min=arr[0]

for i in arr:
    if i>max:
        max=i

for i in arr:
    if i<min:
        min=i

print("Largest=", max)
print("Smallest=", min)