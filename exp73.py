def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
sum,temp=0,0
n=int(input())
temp=n
while n!=0:
    r=n%10
    sum=sum+fact(r)
    n=n//10
    if sum==temp:
        print("strong number")
    else:
        print("not a strong number")