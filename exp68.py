#write a program to print the fibonnaci series using recursion by functions till 7 n
#1 1 2 3 5 8 13
def fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo(n-1) + fibo(n-2))  
n = int(input("enter the terms: "))   
if n <= 1:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(n):  
       print(fibo(i),end=" ")  