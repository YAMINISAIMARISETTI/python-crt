# program to create self argument and acess an object
class xyz:
    var=100
    print(var)
class abc:
    attribute1=10
    def display(self):
        print("this is in class ")
obj=abc()
print(obj.attribute1)
obj.display()
obj=xyz()