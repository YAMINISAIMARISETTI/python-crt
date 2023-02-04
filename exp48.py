#write a program to check whether thegiven input is satisfying the condition of anagram
#test case1:
#listen : silent  
#race:acer
#output:
#true
#true
str1=input()
str2=input()
n=len(str1)
m=len(str2)
x=sorted(str1)
y=sorted(str2)
if n==m:
    if x==y:
        print("anagram")
    else:
        print("not a anagram")
else:
    print("not a anagram as length difference")