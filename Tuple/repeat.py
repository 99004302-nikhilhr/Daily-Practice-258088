tup= (2,4,6,7,8,2,2,7,"LTTS","LTTS","python","c","c","java")
rep=[]
for i in tup:
    if tup.count(i)>1:
        rep.append(i)
    else:
        continue
for x in rep:
    while rep.count(x)>1:
        rep.remove(x)
print("Repeated items:",tuple(rep))