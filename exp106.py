def linear_search(agelist,n,key):
    for i in range(0,n):
        if str(agelist[i])==agelist[i]:
            agelist[i]=ord(agelist[i])
        if(agelist[i] == key):
            return i
        return 100
agelist = ['a',10,30,-50,40,-70,90]
key = 97
n=len(agelist)
res = linear_search(agelist,n,key)
if(res == 100):
    print("age is not found")
else:
    print("age found at index:", res)