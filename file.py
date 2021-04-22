#read #readlines
import random
file = open("one.py", "r")
print(file.read())


f=open("write.py","a")
n=random.randint(1,100)
if n%2==0:
    f.write(str(n)+"\n")
else:
    f.write("Enetr odd No"+"\n")
    print("\n")
file.close()


