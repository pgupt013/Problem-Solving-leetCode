## 268. Find the Missing NUmber 

def missingNumber(a):
    n=len(a)
    sum=n*(n+1)/2
    for i in range(n):
        sum=sum-a[i]
    return sum
a=[9,6,8,2,3,5,7,0,1]
print(missingNumber(a))