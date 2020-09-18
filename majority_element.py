def findMajority(arr,n):
    m_element=0
    count=1
    for i in range(n):
        if arr[i]==m_element:
            count+=1
        else:
            count-=1
        if count==0:
            m_element=arr[i]
            count+=1
    return m_element
def isMajority(arr,n,m_element):
    count=0
    for i in range(n):
        if arr[i]==m_element:
            count+=1
    if count>n/2:
        return True
    else:
        return False
if __name__=='__main__':
    arr=[2,2,1,1,1,2,2]
    value=findMajority(arr,len(arr))
    if(isMajority(arr,len(arr),value)):
        print(value)
    else:
        print("majority element not found")