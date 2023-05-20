# write a program to check whether the given number is even or odd by using a
#singlestance class object with an attribute following a constructor
#test case:21
class xyz:
    def __init__(self,n):
        self.n=n
        if n%2==0:
            print("even")
        else:
            print("odd")
n=int(input())
obj=xyz(n)