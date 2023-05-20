# write a program to check whether the given number is even or odd by using a
#singlestance class object with an attribute following a constructor
#test case:21
class xyz():
    even=0
    def check(self,n):
        if n%2==0:
            self.even=1
    def even_odd(self,n):
            self.check(n)
            if self.even==1:
                print(n,"is even")
            else:
                print(n,"is odd")
n=xyz()
n.even_odd(10)