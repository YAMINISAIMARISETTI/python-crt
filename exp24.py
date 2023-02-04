n=int(input("Enter a number:"))
sum=0
a=0
while(n!=0):
    n=n//10
    a=a+1
while(n>0):
    r=n%10
    sum=sum+r**a
    n=n//10
if sum==n:
    print("Armstrong")
else:
    print("Not a Armstrong")
