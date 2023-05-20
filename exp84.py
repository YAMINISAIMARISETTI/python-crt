#write a program that has a class named circle use class a variable to define
#the values of constant pi.Use this class variable to calculate area and
#circumfernernce of a circle with specify radius where radius=7.5
class circle:
    PI=3.14159
    def __init__(self,r):
        self.r=r
        area=circle.PI*r*r
        circum=2*circle.PI*r
        print(area)
        print(circum)
obj=circle(7.5)