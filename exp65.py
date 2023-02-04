#write a program to add 6 user defined numbers and retun the value to the main program
#test case1:8,6,4,2,10,0
def sum(a,b,c,d,e,f):
    return(a+b+c+d+e+f)
a,b,c,d,e,f=int(input("enter the numbers:").split(" "))
result=sum(a,b,c,d,e,f)
print("result",result)