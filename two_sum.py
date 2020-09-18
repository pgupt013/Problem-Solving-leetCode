num=[2,7,11,15]
#target=9
n=len(num)
def sum(num,target=9):
    for i in range(n):
        for j in range(1,n):
            if num[i]+num[j]==target:
                print(i,j)
sum(num)