#write a program that has a class named circle use class a variable to define
#the values of constant pi.Use this class variable to calculate area and
#circumfernernce of a circle with specify radius where radius=7.5
class circle:
    PI=3.14759
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.PI*self.r*self.r
    def circum(self):
        return 2*circle.PI*self.r
obj=circle(7.5)
print(obj.area())
print(obj.circum())