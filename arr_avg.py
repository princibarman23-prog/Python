n=int(input("Enter the number of subject's marks you want to enter: "))
arr=[]*n 
sum=0
for i in range(n):
    num=float(input(f"Enter the marks of the {i+1} subject: "))
    arr.append(num)

for i in range(n):
    sum=sum + arr[i]

print(f"The Total of the {n} subject is:{sum} ")

print(f"The Average of the {n} subject is:",sum/n)