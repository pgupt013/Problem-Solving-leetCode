arr=[8,4,2,3,1,5,4,2]
temp=len(arr)
max_value=arr[temp-1]
print(max_value)
for i in range(temp-1,-1,-1):
    if arr[i] >max_value:
        max_value=arr[i]
        print(max_value)
    
