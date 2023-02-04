n=int(input("Enter a number:"))
sum=0
var=n
a=0
while(var!=0):
    var=var//10
    a=a+1
var=n
while(var>0):
    r=var%10
    sum=sum+r**a
    var=var//10
if sum==n:
    print("Armstrong")
else:
    print("Not a Armstrong")