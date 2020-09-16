nums = [0,1,2,3,4]
index=[0,1,2,2,1]
target=[]
for i in range(len(nums)):
    if index[i]>=len(index)-1:
        target.append(nums[i])
    else:
        target.insert(index[i],nums[i])
print(target)