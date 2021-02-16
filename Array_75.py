## 75. Sort Colors
## Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
## We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
arr=[2,0,2,1,1,0]
##arr=[2,0,1]
low=0
mid=0
high=len(arr)-1
while mid<=high:
    if arr[mid]==0:
        arr[mid],arr[low]=arr[low],arr[mid]
        low=low+1
        mid=mid+1
    elif arr[mid]==1:
        mid=mid+1
    else: 
        arr[mid]==2
        arr[mid],arr[high]=arr[high],arr[mid]
        high=high-1 
print(arr)