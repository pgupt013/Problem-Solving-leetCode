
def singleNumber(nums):
    res=0
    for i in nums:
        res=res^i
    return res
#nums=[2,3,5,4,5,2,4,3,5,2,4,4,2]
nums=[2,2,1]
print(singleNumber(nums))