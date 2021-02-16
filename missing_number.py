def findMissingNum(a,n):
    x1 = a[0] 
    x2 = 0
 
    for i in range(0, n): 
        x1 = x1 ^ a[i]      #As mentioned in the video we are doing XOR of the array elements
 
    for i in range(0, n): 
        x2 = x2 ^ i        #Now we are applying the xor operation on indices 
 
    return x1 ^ x2          # If you apply XOR of the x1 and x2 then you get the missing number

l=[9,6,8,2,3,5,7,0,1]
n=len(l)
miss=findMissingNum(l,n)
print(miss)