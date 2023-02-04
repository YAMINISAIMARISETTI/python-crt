# program to create self argument and acess an object
class abc:
    attribute1=10
    def display(self):
        print("this is in class ")
obj=abc()
print(obj.attribute1)
obj.display()