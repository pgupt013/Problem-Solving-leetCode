
def reverse(arr,i,j):
    while(i<=j):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1
def rotateKtimes(arr,n,k):
    reverse (arr, n-k, n-1)
    reverse (arr,0, n-k-1)
    reverse (arr, 0, n-1)
    print(arr)
    
if __name__=='__main__':
    arr = [1,2,3,4,5,6]
    rotateKtimes(arr,len(arr),3)
