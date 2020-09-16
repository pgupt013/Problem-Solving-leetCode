num = eval(input("Enter some values"))
print(type(num))
print(enumerate(sorted(num)))

count={}
for k,v in enumerate(sorted(num)):
    print(k,v)
    if v not in count:
        count[v]=k
print(count)  

result=[]
for v in num:
    result.append(count[v])
print(result)

        








