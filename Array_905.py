## 905. Sort Array By Parity
## Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
l=[3,1,2,4]
i=0
j=len(l)-1
print(i,j)
while i<j:
    if l[i]%2 !=0:
        l[i],l[j]=l[j],l[i]
        j=j-1
    else:
        i=i+1
print(l)

