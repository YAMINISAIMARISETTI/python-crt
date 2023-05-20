m=[15,5,10,-5,25,-5,25,-5]
duplicates=[]
for i in m:
    if m.count(i)>1:
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)