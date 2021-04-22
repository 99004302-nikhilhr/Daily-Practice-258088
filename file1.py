file = open("books.txt", "r")

#your code goes here
l=file.readlines()
for i in range(len(l)):
    a=l[i].strip()
    c=0
    for j in range(len(a)):
        c=c+1
    print(a[0]+str(c))

file.close()