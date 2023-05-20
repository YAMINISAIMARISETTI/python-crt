list=[15,5,10,-5,25,-5,25,-5]
count={}
for i in list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)