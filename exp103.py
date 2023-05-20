list=[15,5,10,-5,25,-5,25,-5,97,'a',100,'d',65,'A']
count={}
for i in list:
    if str(i).lower() in ('a','e','i','o','u'):
        if str(i)==i:
            i=ord(i)
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)