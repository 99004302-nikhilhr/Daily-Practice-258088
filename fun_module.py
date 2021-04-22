#Python Basics :

#functions and modules : How to define fun and use arguments.

import random
from random import randint as r
def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))
print(r(1,10))