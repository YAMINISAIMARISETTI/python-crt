from collections import counter
def check(str1,str2):
    if(counter(str1)==counter(str2)):
        print("true")
    else:
       print("not")
str1= 'silent'
str2='listen'
check(str1,str2)