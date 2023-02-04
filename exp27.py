n=int(input("Enter a Number:"))
x=0
y=0
for i in range(1,n+1):
    if(i%2!=0):
        x=x+7
    else:
        y=y+6
if(n%2!=0):
    print(' {} term in the format is {}'.format(n,x-7))
else:
    print(' {} term in the format is {}'.format(n,x-6))