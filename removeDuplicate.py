arr=[0,0,1,1,1,2,2,3,3,3,4,5,5,6]

def removeDuplicates(nums):
    if not nums:
        return 0

    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k+=1

    return k

newArr=arr[:]
count=removeDuplicates(newArr)

print("Original Array:",arr)
print("Number of unique elements:" ,count)
print("Modified Array:" ,newArr[:count])
