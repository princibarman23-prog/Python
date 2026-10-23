arr = [12, 5, 78, 34, 9, 56]

Largest=arr[0]
Smallest=arr[0]
for arr in arr[1:]:
   if arr>Largest:
    Largest=arr
   if arr<Smallest:
    Smallest=arr
print("Largest element is:",Largest)
print("Smallest element is:",Smallest)