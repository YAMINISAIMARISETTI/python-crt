n=int(input("Enter a number:"))
s=0
s1=0
while(n>0):
    r=n%10
    if(n%2==0):
        s=s+r
    else:
        s1=s1+r
    n=n//10
print(abs(s-s1))