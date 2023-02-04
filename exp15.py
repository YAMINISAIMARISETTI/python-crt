x=int(input("Enter a number:"))
s=0
while(x!=0):
    r=x%10
    s=s+r**3
    x=x//10
if(s==x):
    print(x,"is Armstrong")
else:
    print(x,"is not Armstrong")