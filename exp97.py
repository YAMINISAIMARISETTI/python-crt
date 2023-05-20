a=[1,2,5,3,10,15,20]
for i in range(len(a)+1):
    if(a[i]%5 == 0):
        a.insert(i+1,7)
print(a)