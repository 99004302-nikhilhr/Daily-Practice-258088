#Merge Two dictionaries
d1={1:"virat",2:"padikal",3:"ABD",4:"Maxwell"}
d2={5:"MSD",6:"Raina",7:"Jaddu",8:"Bravo"}
for i in d2.keys():
    d1[i]=d2[i]
print(d1)
