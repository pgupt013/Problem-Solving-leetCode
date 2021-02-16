## 169. Majority Element

def majorityElement(nums):
    n=len(nums)
    m_element=0
    count=1
    for i in range(n):
        if nums[i]==m_element:
            count+=1
        else:
            count-=1
        if count==0:
            m_element=nums[i]
            count+=1
    return m_element

#nums=[2,2,1,1,1,2,2]
nums=[3,2,3]
x=majorityElement(nums)
print(x)

