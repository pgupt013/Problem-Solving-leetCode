s='aaaabbcccccdeffff'
n= len(s)
i=0
result=""
while i<n:
    count=1
    while(i+1<n and s[i]==s[i+1]):
        count=count+1
        i=i+1
    result=s[i]+str(count)
    print(result,end='')
    i=i+1