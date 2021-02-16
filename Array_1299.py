## 1299. Replace Elements with Greatest Element on Right Side
#arr = [17,18,5,4,6,1]
arr=[400]
n= len(arr)
max_element= arr[n-1]
arr[n-1]=-1
for i in range(n-2,-1,-1):
    temp=arr[i]
    arr[i]=max_element
    if temp> max_element:
        max_element=temp
    
print(arr)