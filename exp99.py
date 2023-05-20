marks=[15,5,10,-5]
for i in range(len(marks)):
    for j in range(i+1,len(marks)):
        if(marks[i]>marks[j]):
            marks[i],marks[j]=marks[j],marks[i]
print(marks)